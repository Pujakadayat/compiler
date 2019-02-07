import parser.classes as classes
import parser.grammar as grammar
import tokens as TokenTypes


import time


def parse(tokens):
    parser = Parser(tokens)
    parser.parse()


class Parser:
    def __init__(self, tokens):
        self.stack = []
        self.tokens = tokens

    def parse(self):
        if len(self.stack) == 1:
            self.reduce()

            # Check if we can't reduce anymore (accept state)
            if isinstance(self.stack[0], classes.Program):
                print("✨ Completed parsing!")
                print(self.stack)
                print(self.stack[0].declarations)
                return

        # Recursively parse until accept state
        self.shift()
        self.reduce()
        self.parse()

    def shift(self):
        print(f"Before shift: {self.stack}")
        self.stack.append(self.tokens.pop(0))
        print(f"After shift: {self.stack}")

    def reduce(self):
        # Check [int], then [int, main], then [int, main, (] etc...
        for index in range(len(self.stack), 0, -1):
            # Current stack contains subset of stack increasing from R -> L
            currentStack = self.stack[index - 1 : len(self.stack)]

            print(f"Current stack: {currentStack}")

            # Check grammar rules on current stack
            for rule in grammar.rules:
                print(f"Checking rule: {rule}")
                # Apply the rule to our current stack
                token = rule(currentStack)

                # If the rule matched...
                if token:
                    print("\n FOUND A MATCHING RULE \n")
                    # Replace the actual stack
                    self.stack[index - 1 : len(self.stack)] = [token]

                    break
                else:
                    continue
