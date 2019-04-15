"""
Methods and classes related to
Intermediate Representations of the Parse Tree.
"""

import src.util as util
import src.parser.grammar as grammar


class IR:
    """Intermediate Representation class to hold IR data."""

    def __init__(self, parseTree):
        self.parseTree = parseTree
        self.stack = []
        self.ir = {}
        self.current = None

    def generate(self):
        """Generate the IR from the parse tree."""

        self.visit(self.parseTree)

        for x in self.ir:
            print("---")
            print(x)
            for i in self.ir[x]["blocks"]:
                print(i)

        return self.ir

    def closeBlock(self):
        """Save the stack as a block and start a new block."""

        if self.stack:
            self.ir[self.current]["blocks"].append(self.stack)

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
            print(f"checking {node}")

            # End the basic blocks we created earlier now that all
            # the node within have been visited.
            if isinstance(node, grammar.FunctionDeclaration):
                self.ir[node.name]["arguments"] = node.arguments.value
                self.closeBlock()
            elif isinstance(node, grammar.IfStatement):
                self.closeBlock()
            elif isinstance(node, grammar.Condition):
                self.stack.append(f"if r{util.count['none']} is true")
                self.closeBlock()
            elif isinstance(node, grammar.ElseStatement):
                self.closeBlock()
            elif isinstance(node, grammar.LabelDeclaration):
                self.stack.insert(0, node.ir())
                self.closeBlock()
            else:
                i = node.ir()
                if i is not None and not i.isdigit():
                    self.stack.append(i)

    def print(self):
        """Print the intermediate representation as a string."""

        for function in self.ir:
            print(f".{function} ({self.ir[function]['arguments']})")
            for block in self.ir[function]["blocks"]:
                for line in block:
                    print(line)

    def __str__(self):
        s = []

        for function in self.ir:
            s.append(f".{function} ({self.ir[function]['arguments']})")
            for block in self.ir[function]["blocks"]:
                for line in block:
                    s.append(line)

        return "\n".join(s)
