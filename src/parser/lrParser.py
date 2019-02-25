# http://www.orcca.on.ca/~watt/home/courses/2007-08/cs447a/notes/LR1%20Parsing%20Tables%20Example.pdf
# used this to write this file

import getopt
import logging
import sys
import os
import json

debug = False


# This class will generate the action and goto tables
class LRParser:
    def __init__(self):
        # Rules parsed from grammar
        self.rules = {}

        # Nessisary variables to generate acion and goto tables
        self.itemSets = {}
        self.transitions = {}
        self.setNum = 0
        self.terminals = []
        self.nonTerminals = []

        # Action and goto tables
        self.actions = {}
        self.goto = {}

    def buildTables(self):
        # Start itemset 0 with the accepting state
        self.itemSets[0] = [item("ACC", "program", 0, "$")]

        # close Itemsets and create new sets until no more
        i = 0
        while i <= max(self.itemSets.keys()):
            if self.hasItemSet(i):
                # close out itemset i
                self.closure(i)
                # change nonterminal followers to terminals in itemset i
                self.cleanItemSet(i)
                # create any new itemsets from itemset i
                self.createItemSets(i)
                # search through itemsets and remove any copies
                self.cleanItemSets()
            i = i + 1

        # build tables
        self.buildActionGoto()

        self.printRules()
        # self.printItemSets()
        # self.printTransitions()
        self.printTable()

    # parse the input grammar into rules
    #   the variable self.rules is filled here
    #   self.rules in a dictionary with the lhs of a rule as the key
    #   and lists as the value. The lists are the different rhs's that
    #   the rule points to.
    def parseGrammar(self, grammar):
        # Augment rules with accepting state
        self.rules["ACC"] = [["program"]]

        # Open file with grammar
        lines = grammar.splitlines()

        # parse grammar file into rules
        for line in lines:
            if line == "":
                # Skip blank lines
                continue
            elif line[0] == "#":
                # Skip comment lines
                continue

            rule = line.split(" ")
            # Check to see if valid format
            if rule[1] == "->":
                # seperate the "|" out of the rule
                last = 2
                for i in range(len(rule)):
                    if rule[i] == "|":
                        # if lhs of rule is in self.rules, append rhs of rule to the list
                        if rule[0] in self.rules.keys():
                            self.rules[rule[0]].append(rule[last:i])
                        # if lhs of rule is not in self.rules, add new dictionary element
                        else:
                            self.rules[rule[0]] = [rule[last:i]]
                        last = i + 1
                # for loop above catches all but the last rule from the grammar
                # this if-else is to catch that final rule
                if rule[0] in self.rules.keys():
                    self.rules[rule[0]].append(rule[last:])
                else:
                    self.rules[rule[0]] = [rule[last:]]

        # add all the nonTerminals to self.nonTerminal list
        for k in self.rules.keys():
            if k not in self.nonTerminals:
                self.nonTerminals.append(k)

        # add all the terminals to the self.terminals list
        for v in self.rules.values():
            for tokenList in v:
                for token in tokenList:
                    if token not in self.nonTerminals and token not in self.terminals:
                        self.terminals.append(token)

    # close out an itemset
    # this involves expanding out rules from the grammar
    def closure(self, setNum):
        if debug:
            print("closing out itemset", setNum)
        # newSet is just the itemset we are currently interested in
        newSet = self.itemSets[setNum]
        done = False
        # keep looping until no more rules can be expanded
        while not done:
            # for each item in the set:
            for currItem in newSet:
                new = False
                # get the token after the dot
                a = currItem.getRightAfter()
                # get all the tokens after the token after the dot
                b = currItem.getAfter()
                # following becomes the first token after the token after the seperator
                # if there is a token after the token after the seperator
                # if not, following is just the o
                following = currItem.following
                if len(b) > 0:
                    following = b[0]
                # if a is a nonTerminal, expand rule
                if a in self.rules.keys():
                    new = True
                    # for each rule for nonTerminal a:
                    for rule in self.rules[a]:
                        # make a new item for nonTerminal a rule
                        rhs = " ".join(rule)
                        newItem = item(a, rhs, 0, following)
                        # check if item already exists in the itemSet
                        isNew = True
                        for tempItem in newSet:
                            if newItem.isSame(tempItem):
                                isNew = False
                        # if item is new then add it to set
                        if isNew:
                            newSet.append(newItem)
                            new = True
                            # print("\t", newItem)
                # if no new items found we are done
                if not new:
                    done = True

    # remove any nonterm following token from itemSet
    def cleanItemSet(self, setNum):
        nonTerms = True
        # loop until no more nonTerminal following tokens found in itemset
        while nonTerms:
            nonTerms = False
            for itemNum in range(len(self.itemSets[setNum])):
                # if item.following in itemSet is a nonTerm then expand the nonTerm into terminal
                if self.itemSets[setNum][itemNum].following in self.nonTerminals:
                    nonTerms = True
                    lhs = self.itemSets[setNum][itemNum].lhs
                    rhs = self.itemSets[setNum][itemNum].rhs
                    sep = self.itemSets[setNum][itemNum].seperator
                    following = self.itemSets[setNum][itemNum].following
                    # for each rule the nonTerminal token expands into:
                    for numRule in range(len(self.rules[following])):
                        newItem = item(lhs, rhs, sep, self.rules[following][numRule][0])
                        # check to see if new item is new to the set
                        isNew = True
                        for tempItem in self.itemSets[setNum]:
                            if newItem.isSame(tempItem):
                                isNew = False
                        # if it is, add it to the itemSet
                        if isNew:
                            self.itemSets[setNum].append(newItem)
                    # delete the old rule with the nonTerminal following token
                    del self.itemSets[setNum][itemNum]
                    break

    # create new itemSets from past itemSets
    # this is tracked with the transition table
    def createItemSets(self, setNum):
        # for each item in itemSet[setNum]
        for currItem in self.itemSets[setNum]:
            # make a newItem from the currItem with the seperator incremented by 1
            newItem = currItem.incSeperator()
            # get the delimeter for the transition table
            delimeter = newItem.getRightBefore()
            # if delimeter exists
            if len(delimeter) > 0:
                # if the transitions for itemSet[setNum] does not exist add it
                if setNum not in self.transitions.keys():
                    self.transitions[setNum] = {}
                # if delimeter does not exist in transition[setNum] add it and increment self.setNum by 1
                if delimeter not in self.transitions[setNum].keys():
                    self.setNum = self.setNum + 1
                    self.transitions[setNum][delimeter] = self.setNum
                # if the new itemSet does not exist in self.itemSets add it
                if self.transitions[setNum][delimeter] not in self.itemSets.keys():
                    self.itemSets[self.transitions[setNum][delimeter]] = []
                # add the newItem to the new set
                self.itemSets[self.transitions[setNum][delimeter]].append(newItem)

    # clean itemSets of any identical sets
    def cleanItemSets(self):
        # compare the itemSets backwards
        # So compare every set with the sets that came before it
        for i in range(self.setNum, -1, -1):
            for j in range(i - 1, -1, -1):
                # compare set i with set j
                same = True
                for itemSet in self.itemSets[j]:
                    inThere = False
                    for itemSetCheck in self.itemSets[i]:
                        if itemSetCheck.isSame(itemSet):
                            inThere = True
                    if not inThere:
                        same = False
                        break
                # if itemSets i and j are identical delete itemSet i (the itemSet that came later)
                if same:
                    if debug:
                        print("Replacing itemset", i, "with itemset", j)
                    del self.itemSets[i]
                    # self.setNum is now the lowest available set number
                    self.updateSetNum()
                    # update the transition table so any reference of itemSet i becomes itemSet j
                    for k1, v1 in self.transitions.items():
                        for k2, v2 in v1.items():
                            if self.transitions[k1][k2] == i:
                                self.transitions[k1][k2] = j
                    break

    # build the action and goto tables from the itemSets and the transition table
    def buildActionGoto(self):
        # go through itemSets to get reduction rules
        for itemSetNum, itemSet in self.itemSets.items():
            for item in itemSet:
                if self.seperatorAtEnd(item):
                    for k, v in self.rules.items():
                        if item.lhs == k:
                            for i in range(len(v)):
                                if item.rhs == " ".join(v[i]):
                                    if itemSetNum not in self.actions.keys():
                                        self.actions[itemSetNum] = {}
                                    self.actions[itemSetNum][
                                        item.following
                                    ] = "r %s %i" % (k, i)

        # go through transition table to get:
        for k1, v1 in self.transitions.items():
            for k2, v2 in v1.items():
                # goto rules
                if k2 in self.nonTerminals:
                    if k1 not in self.goto.keys():
                        self.goto[k1] = {}
                    self.goto[k1][k2] = v2
                # shift rules
                else:
                    if k1 not in self.actions.keys():
                        self.actions[k1] = {}
                    self.actions[k1][k2] = "s %i" % (v2)

    def loadParseTables(self, grammarFile, force=False):
        grammarName = grammarFile.split("/")[1].split(".")[0]
        tableFile = "{}{}{}".format("tables/", grammarName, "_table.json")

        # Parse the input grammar
        self.parseGrammar(readFile(grammarFile))

        if os.path.isfile(tableFile) and force is False:
            # Load a saved tables file
            print("✔ Reading saved tables...")
            self.loadTables(readFile(tableFile))
        else:
            # Parse the tokens using an LR(1) table
            print("✖ Generating new tables...")
            self.buildTables()
            self.saveTables(tableFile)

    def saveTables(self, tableFileName):
        with open(tableFileName, "w") as outfile:
            # Save the action table
            json.dump(self.actions, outfile)
            outfile.write("\n")

            # Save the goto table
            json.dump(self.goto, outfile)

    def loadTables(self, tableFile):
        lines = tableFile.splitlines()
        tempActions = json.loads(lines[0])
        for key, value in tempActions.items():
            self.actions[int(key)] = value
        tempGoto = json.loads(lines[1])
        for key, value in tempGoto.items():
            self.goto[int(key)] = value

    def parse(self, tokens):
        lookahead = 0
        done = False
        states = [0]
        output = []
        stack = []

        while not done:
            state = states[len(states) - 1]
            token = tokens[lookahead]
            if token.kind.desc() in self.terminals:
                token = token.kind.desc()
            else:
                token = token.content

            print(
                "---\nState:",
                state,
                "\nStates:",
                states,
                "\nlookahead Token:",
                token,
                "\nstack:",
                stack,
                "\noutput:",
                output,
            )

            try:
                # Check if we have an entry in our action table for the lookahead token
                if token in self.actions[state].keys():
                    result = self.actions[state][token]
                    output.append(result)
                    result = result.split(" ")

                    # If the action table says to shift, shift the next token
                    if result[0] == "s":
                        states.append(int(result[1]))
                        stack.append(token)
                        lookahead += 1
                        print("Shifting")

                    # If the action table says to reduce
                    if result[0] == "r":
                        # Get the corresponding rule from our rules table
                        rule = self.rules[result[1]][int(result[2])]

                        # Check if the tokens on the stack match a grammar rule
                        match = True
                        for i in range(len(rule)):
                            if rule[i] != stack[len(stack) - len(rule) + i]:
                                match = False

                        # If one of the grammar rules matched...
                        if match:
                            # Reduce the tokens on the stack to our new rule token
                            del stack[len(stack) - len(rule) : len(stack)]
                            del states[len(states) - len(rule) : len(states)]
                            stack.append(result[1])
                            print("Reducing rule", result[1], "->", rule)

                            # Check if there is a goto rule for our current state
                            topState = states[-1]
                            topStack = stack[-1]
                            if topStack in self.goto[topState].keys():
                                states.append(self.goto[topState][topStack])
                else:
                    print("ERROR: State", state, "Token", token)
                    print(self.actions[state])
                    break
            except KeyError:
                print(f"No entry in the action table for state: {state}")
                break

            # Check if we have reached the accepting state
            if len(stack) == 1 and stack[0] == "ACC":
                done = True

        print(output)

    def updateSetNum(self):
        i = 0
        while self.hasItemSet(i):
            i = i + 1
        self.setNum = i - 1

    def hasItemSet(self, num):
        if num in self.itemSets.keys():
            return True
        else:
            return False

    def seperatorAtEnd(self, currItem):
        if currItem.seperator >= len(currItem.rhs.split(" ")):
            return True
        else:
            return False

    def printRules(self):
        print("--- Rules ---")
        for k, v in self.rules.items():
            print(k, ": ", v)
        print("--- NonTerminals ---")
        for nt in self.nonTerminals:
            print(nt)
        print("--- Terminals ---")
        for t in self.terminals:
            print(t)

    def printItemSets(self):
        print("--- Items ---")
        for itemSetNum, itemSet in self.itemSets.items():
            print("Item Set %i: " % (itemSetNum))
            for item in itemSet:
                print("\t", item)

    def printTransitions(self):
        print("--- Transitions ---")
        for k, v in self.transitions.items():
            print(k, v)
            # for tokenK,tokenV in v.items():
            #    print ("\n%s:%i"%(tokenK, tokenV))

    def printTable(self):
        print("--- Actions ---")
        for k, v in self.actions.items():
            print(k, v)
        print("--- Goto ---")
        for k, v in self.goto.items():
            print(k, v)


# an item is like a grammar rule
# there is a left hand side of the rule (lhs)
# and a right hand side (rhs)
# a seperator that is the dot thing
# and a following token for the rule
class item:
    def __init__(self, lhs, rhs, seperator, following):
        self.lhs = lhs
        self.rhs = rhs
        self.seperator = seperator
        self.following = following

    def __str__(self):
        rhs = self.rhs.split(" ")
        return "[%s -> %s.%s, %s]" % (
            self.lhs,
            " ".join(rhs[0 : self.seperator]),
            " ".join(rhs[self.seperator : len(self.rhs)]),
            self.following,
        )

    def isSame(self, tempItem):
        if (
            tempItem.lhs == self.lhs
            and tempItem.rhs == self.rhs
            and tempItem.seperator == self.seperator
            and tempItem.following == self.following
        ):
            return True
        else:
            return False

    def getRightBefore(self):
        rhs = self.rhs.split(" ")
        if self.seperator - 1 < 0 or self.seperator - 1 >= len(rhs):
            return ""
        return rhs[self.seperator - 1]

    def getRightAfter(self):
        rhs = self.rhs.split(" ")
        if self.seperator >= len(rhs):
            return ""
        return rhs[self.seperator]

    def getAfter(self):
        rhs = self.rhs.split(" ")
        return rhs[self.seperator + 1 : len(self.rhs)]

    def incSeperator(self):
        return item(self.lhs, self.rhs, self.seperator + 1, self.following)


def readFile(filename):
    try:
        with open(filename) as file:
            return file.read()
    except IOError as err:
        print(err)
        print(f"Could not read the file: {filename}")
        sys.exit(2)
