import parser.grammar as grammar
import tokens as TokenTypes
import time
import logging
import pprint

debug = True

class Parser:
    def __init__(self, tokens):
        self.stack = []
        self.tokens = tokens

    def parse(self):
        # If we only have 1 token, avoid shifting
        if len(self.stack) == 1:
            self.reduceToken()

            # Check if we can't reduce anymore (accept state)
            if isinstance(self.stack[0], grammar.Program):
                if debug is True:
                    logging.debug("✨ Completed parsing!")
                    logging.debug(self.stack)
                    logging.debug(self.stack[0].declarations)
                return

        # Recursively parse until accept state
        self.shiftToken()
        self.reduceToken()
        self.parse()

    def shiftToken(self):
        if debug is True:
            logging.debug(f"Before shift: {self.stack}")
        self.stack.append(self.tokens.pop(0))
        if debug is True:
            logging.debug(f"After shift: {self.stack}")

    def reduceToken(self):
        # Check [int], then [int, main], then [int, main, (] etc...
        for index in range(len(self.stack), 0, -1):
            # Current stack contains subset of stack increasing from R -> L
            currentStack = self.stack[index - 1 : len(self.stack)]

            if debug is True:
                logging.debug(f"Current stack: {currentStack}")

            # Check grammar rules on current stack
            for rule in grammar.rules:
                if debug is True:
                    logging.debug(f"Checking rule: {rule}")

                # Apply the rule to our current stack
                token = rule.parse(currentStack)

                # If the rule matched...
                if token:
                    if debug is True:
                        logging.debug("\n FOUND A MATCHING RULE \n")

                    # Replace the actual stack
                    self.stack[index - 1 : len(self.stack)] = [token]

                    break
                else:
                    continue

    def print(self):
        for token in self.stack:
            token.prettyPrint(0)
            #if not isinstance(grammar.TypeSpecifier, grammar.NUMCONST):
            #    return None

            #else:
            #    print(token)
            #    pp = pprint.PrettyPrinter(indent=8)
            #    pp.pprint(token)
            #    print("are you getting here??")
