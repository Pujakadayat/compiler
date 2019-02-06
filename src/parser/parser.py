import parser.classes as classes
import parser.grammar as grammar


def parse(tokens):
    parser = Parser(tokens)
    parser.parse()


class Parser:
    def __init__(self, tokens):
        self.stack = []
        self.tokens = tokens

    def parse(self):
        print("Parse me!")
        return

        # Check if we can't reduce anymore (accept state)
        if len(self.stack) == 1:
            if isinstance(self.stack[0], classes.Program):
                print("✨ Completed parsing!")
                return

        # Recursively parse until accept state
        self.shift()
        self.reduce()
        self.parse()

    def shift(self):
        self.stack.append(self.tokens.pop())

    def reduce(self):
        index = 0

        for index in range(len(self.stack)):
            # Current stack contains subset of stack increasing from L -> R
            currentStack = self.stack[:index]

            # Check grammar rules on current stack
            for rule in grammar:
                # Apply the rule to our current stack
                token = rule(currentStack)

                # If the rule matched...
                if token:
                    # Replace the actual stack
                    self.stack[:index] = token

                    break
                else:
                    continue
