"""
Methods and classes related to
Intermediate Representations of the Parse Tree.
"""

import src.util as util
import src.parser.grammar as grammar


class BasicBlock:
    """Defines a set of instructions and data that compose a Basic Block."""

    def __init__(self, instructions, label=None):
        self.instructions = instructions
        self.label = label
        self.instructions.insert(0, ("label", label))

    def print(self):
        """Print this basic block."""

        for i in self.instructions:
            print(i)
        print()


class IR:
    """Intermediate Representation class to hold IR data."""

    def __init__(self, parseTree):
        self.parseTree = parseTree
        self.stack = []
        self.ir = {}
        self.current = None

    def generate(self):
        """Generate the IR from the parse tree."""

        self.parseTree.visit()
        self.visit(self.parseTree)

        return self.ir

    def closeBlock(self):
        """Save the stack as a block and start a new block."""

        if self.stack:
            bb = BasicBlock(self.stack, util.unique("_L"))
            self.ir[self.current]["blocks"].append(bb)

        self.stack = []

    def visit(self, node):
        """Visit a node of the parse tree and recurse."""

        # Start new basic blocks when we first encounter certain nodes.
        if isinstance(node, grammar.FunctionDeclaration):
            # Start a new function entry
            self.ir[node.name] = {}
            self.ir[node.name]["blocks"] = []
            self.current = node.name
        elif isinstance(node, grammar.IfStatement):
            self.closeBlock()
        elif isinstance(node, grammar.ElseStatement):
            self.closeBlock()
        elif isinstance(node, grammar.LabelDeclaration):
            self.closeBlock()
        elif isinstance(node, grammar.Condition):
            self.closeBlock()
        elif isinstance(node, grammar.WhileStatement):
            self.closeBlock()
        elif isinstance(node, grammar.WhileCondition):
            self.closeBlock()

        # Slide to the left, slide to the right
        # Recurse recurse, recurse recurse!
        # ~ Dj Casper (Cha Cha Slide)
        if hasattr(node, "children"):
            for child in node.children:
                self.visit(child)
        elif isinstance(node, list):
            for child in node:
                self.visit(child)

        if not isinstance(node, list):
            # End the basic blocks we created earlier now that all
            # the node within have been visited.
            if isinstance(node, grammar.FunctionDeclaration):
                self.ir[node.name]["arguments"] = node.arguments.value
                self.closeBlock()
            elif isinstance(node, grammar.IfStatement):
                self.closeBlock()
            elif isinstance(node, grammar.Condition):
                if "_L" in util.count:
                    c = util.count["_L"]
                else:
                    c = 0

                i = (
                    "if",
                    f"r{util.count['none']}",
                    "GOTO",
                    f"_L{c + 2}",
                    "else",
                    "GOTO",
                    f"_L{c + 3}",
                )
                self.stack.append(i)
                self.closeBlock()
            elif isinstance(node, grammar.ElseStatement):
                self.closeBlock()
            elif isinstance(node, grammar.LabelDeclaration):
                self.stack.insert(0, node.ir())
                self.closeBlock()
            elif isinstance(node, grammar.WhileStatement):
                # Must have a goto at the end of while statements
                # to revisit the condition
                self.stack.append(("goto", f"_L{util.count['_L']}"))
                self.closeBlock()
            elif isinstance(node, grammar.WhileCondition):
                self.stack.append(
                    (
                        "if",
                        f"r{util.count['none']}",
                        "GOTO",
                        f"_L{util.count['_L'] + 2}",
                        "else",
                        "GOTO",
                        f"_L{util.count['_L'] + 3}",
                    )
                )
                self.closeBlock()
            else:
                i = node.ir()
                if i is not None:
                    self.stack.append(i)

    def print(self):
        """Print the intermediate representation as a string."""

        print("```")
        for function in self.ir:
            print(f".{function} ({self.ir[function]['arguments']})")
            print()  # Differentiate between basic blocks
            for block in self.ir[function]["blocks"]:
                block.print()
        print("```")

    def __str__(self):
        s = []

        for function in self.ir:
            s.append(f".{function} ({self.ir[function]['arguments']})")
            for block in self.ir[function]["blocks"]:
                for line in block:
                    s.append(line)

        return "\n".join(s)
