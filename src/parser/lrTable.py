# http://www.orcca.on.ca/~watt/home/courses/2007-08/cs447a/notes/LR1%20Parsing%20Tables%20Example.pdf
# used this to write this file

import tokens as tokens
from tokens import Token, TokenType
import logging
import sys

debug = True

# This main function is just for testing
def main():
    lrt = LRTable()
    lrt.buildTable()

# This class will generate the action and goto tables
class LRTable:
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

    def buildTable(self):
        # Augment rules with accepting state
        self.rules["ACC"] = [["program"]]

        # Parse the input grammar
        self.parseGrammar()

        # Add the accepting state to grammar
        self.itemSets[0] = [item("ACC", "program", 0, "$")]

        # close Itemsets and create new sets until no more
        i = 0
        while self.hasItemSet(i):
            self.closure(i)
            self.createSets(i)
            self.cleanItemSets()
            i = i + 1

        # build tables
        self.buildActionGoto()

        self.printRules()
        self.printItems()
        self.printTransitions()
        self.printTable()


    def parseGrammar(self):
        # Open file with grammar
        file = open("src/parser/grammar.txt", "r")

        # parse grammar file into rules
        for line in file:
            rule = line[:-1].split(" ")
            if rule[1] == "->":
                # seperate | in the rule
                last = 2
                for i in range(len(rule)):
                    if rule[i] == "|":
                        if rule[0] in self.rules.keys():
                            self.rules[rule[0]].append(rule[last:i])
                        else:
                            self.rules[rule[0]] = [rule[last:i]]
                        last = i+1
                if rule[0] in self.rules.keys():
                    self.rules[rule[0]].append(rule[last:])
                else:
                    self.rules[rule[0]] = [rule[last:]]
        for k in self.rules.keys():
            if k not in self.nonTerminals:
                self.nonTerminals.append(k)
        for v in self.rules.values():
            for tokenList in v:
                for token in tokenList:
                    if token not in self.nonTerminals and token not in self.terminals:
                        self.terminals.append(token)


    # close out an itemset
    def closure(self, setNum):
        newSet = self.itemSets[setNum]
        done = False
        while not done:
            for i in newSet:
                #print(i)
                new = False
                a = i.getRightAfter()
                b = i.getAfter()
                following = i.following
                if len(b) > 0:
                    following = b[0]
                if a in self.rules.keys():
                    new = True
                    for rule in self.rules[a]:
                        rhs = " ".join(rule)
                        newItem = item(a, rhs, 0, following)
                        isNew = True
                        for tempItem in newSet:
                            if newItem.isSame(tempItem):
                                isNew = False
                        if isNew:
                            newSet.append(newItem)
                            new = True
                            #print("\t", newItem)
                if not new:
                    done = True
        return newSet

    def createSets(self, setNum):
        for currItem in self.itemSets[setNum]:
            newItem = currItem.incSeperator()
            delimeter = newItem.getRightBefore()
            if len(delimeter) > 0:
                if setNum not in self.transitions.keys():
                    self.transitions[setNum] = {}
                if delimeter not in self.transitions[setNum].keys():
                    self.setNum = self.setNum + 1
                    self.transitions[setNum][delimeter] = self.setNum
                #self.printTransitions()
                if self.transitions[setNum][delimeter] not in self.itemSets.keys():
                    self.itemSets[self.transitions[setNum][delimeter]] = []
                self.itemSets[self.transitions[setNum][delimeter]].append(newItem)


    def cleanItemSets(self):
        for i in range(self.setNum, -1, -1):
            for j in range(i-1, -1, -1):
                same = True
                for itemSet in self.itemSets[j]:
                    inThere = False
                    for itemSetCheck in self.itemSets[i]: 
                        if itemSetCheck.isSame(itemSet):
                            inThere = True
                    if not inThere:
                        same = False
                        break
                if same:
                    #print(i, " is the same as ", j)
                    del self.itemSets[i]
                    #self.printItems()
                    self.updateSetNum()
                    #print("u ", self.setNum)
                    for k1, v1 in self.transitions.items():
                        for k2, v2 in v1.items():
                            if self.transitions[k1][k2] == i:
                                self.transitions[k1][k2] = j
                                #print(k1, k2)
                    break

    def buildActionGoto(self):
        for itemSetNum, itemSet in self.itemSets.items():
            for item in itemSet:
                if self.seperatorAtEnd(item):
                    #print("[", itemSetNum, item, "]")
                    for k, v in self.rules.items():
                        if item.lhs == k:
                            #print("found rules", k, v, "for item")
                            for i in range(len(v)):
                                #print("maybe: ", item.rhs, " == ", v[i], "?")
                                if item.rhs == " ".join(v[i]):
                                    #print("This rule: ", self.rules[k][i])
                                    if itemSetNum not in self.actions.keys():
                                        self.actions[itemSetNum] = {}
                                    self.actions[itemSetNum][item.following] = "r %s %i"%(k, i)
        for k1,v1 in self.transitions.items():
            #print(k1)
            for k2,v2 in v1.items():
                #print(k2, v2)
                if k2 in self.nonTerminals:
                    if k1 not in self.goto.keys():
                        self.goto[k1] = {}
                    self.goto[k1][k2] = v2
                else:
                    if k1 not in self.actions.keys():
                        self.actions[k1] = {}
                    self.actions[k1][k2] = "s %i"%(v2)


    def parse(self, scannedTokens):
        scannedTokens.append(Token(tokens.eof, "$"))
        output = []
        stack = []
        states = [0]
        done = False
        lookahead = 0

        while not done:
            state = states[len(states)-1]
            token = scannedTokens[lookahead] 
            if token.kind.desc() in self.terminals:
                token = token.kind.desc()
            else:
                token = token.content
                
            print("---\nState:", state, "\nStates:", states, "\nlookahead Token:", token, "\nstack:", stack, "\noutput:", output)
            if token in self.actions[state].keys():
                result = self.actions[state][token]
                output.append(result)
                result = result.split(" ")
                if result[0] == "s":
                    states.append(int(result[1]))
                    stack.append(token)
                    lookahead = lookahead + 1
                if result[0] == "r":
                    rule = self.rules[result[1]][int(result[2])]
                    #print("rule:", rule)
                    match = True
                    for i in range(len(rule)):
                        if rule[i] != stack[len(stack)-len(rule)+i]:
                            match = False
                    if match:
                        del stack[len(stack)-len(rule):len(stack)]
                        stack.append(result[1])
                        del states[len(states)-len(rule):len(states)]
                        topState = states[len(states)-1]
                        topStack = stack[len(stack)-1]
                        if topStack in self.goto[topState].keys():
                            states.append(self.goto[topState][topStack])
            else:
                print("\terror")
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
        for k,v in self.rules.items():
            print(k, ": ", v)
        print("--- NonTerminals ---")
        for nt in self.nonTerminals:
            print(nt)
        print("--- Terminals ---")
        for t in self.terminals:
            print(t)
        

    def printItems(self):
        print("--- Items ---")
        for itemSetNum, itemSet in self.itemSets.items():
            print("Item Set %i: "%(itemSetNum))
            for item in itemSet:
                print("\t", item)

    def printTransitions(self):
        print("--- Transitions ---")
        for k,v in self.transitions.items():
            print(k, v)
            #for tokenK,tokenV in v.items():
            #    print ("\n%s:%i"%(tokenK, tokenV))

    def printTable(self):
        print("--- Actions ---")
        for k,v in self.actions.items():
            print(k, v)
        print("--- Goto ---")
        for k,v in self.goto.items():
            print(k, v)

class item:
    def __init__(self, lhs, rhs, seperator, following):
        self.lhs = lhs
        self.rhs = rhs
        self.seperator = seperator
        self.following = following

    def __str__(self):
        rhs = self.rhs.split(" ")
        return "[%s -> %s.%s, %s]"%(self.lhs, " ".join(rhs[0:self.seperator]), " ".join(rhs[self.seperator:len(self.rhs)]), self.following)

    def isSame(self, tempItem):
        if tempItem.lhs == self.lhs and tempItem.rhs == self.rhs and tempItem.seperator == self.seperator and tempItem.following == self.following:
            return True
        else:
            return False
        

    def getRightBefore(self):
        rhs = self.rhs.split(" ")
        if self.seperator-1 < 0 or self.seperator-1 >= len(rhs):
            return ""
        return rhs[self.seperator-1]

    def getRightAfter(self):
        rhs = self.rhs.split(" ")
        if self.seperator >= len(rhs):
            return ""
        return rhs[self.seperator]

    def getAfter(self):
        rhs = self.rhs.split(" ")
        return rhs[self.seperator+1:len(self.rhs)]

    def incSeperator(self):
        return item(self.lhs, self.rhs, self.seperator+1, self.following)

if __name__ == "__main__":
    sys.exit(main())
