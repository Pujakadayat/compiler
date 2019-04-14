"""
Methods and classes related to
Intermediate Representations of the Parse Tree.
"""

import src.parser.grammar as grammar


class IR:
    """Intermediate Representation class to hold IR data."""

    def __init__(self, parseTree):
        self.parseTree = parseTree
        self.ir = []
        self.stack = []
        self.table = {}
        self.current = None

    def generate(self):
        """Generate the IR from the parse tree."""

        self.visit(self.parseTree)
        print(self.table)

        return None

    def visit(self, node):
        """Visit a node of the parse tree and recurse."""

        # Start new basic blocks when we first encounter certain nodes.
        if isinstance(node, grammar.FunctionDeclaration):
            # Start a new function entry
            self.table[node.name] = {}
            self.table[node.name]["blocks"] = []
            self.current = node.name
        elif isinstance(node, grammar.IfStatement):
            # Save the stack as a block and start a new one.
            self.table[self.current]["blocks"].append(self.stack)
            self.stack = []
        elif isinstance(node, grammar.ElseStatement):
            self.table[self.current]["blocks"].append(self.stack)
            self.stack = []
        elif isinstance(node, grammar.LabelDeclaration):
            self.table[self.current]["blocks"].append(self.stack)
            self.stack = []

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
                self.table[node.name]["arguments"] = node.arguments.value
                self.table[node.name]["blocks"].append(self.stack)
                self.stack = []
            elif isinstance(node, grammar.IfStatement):
                self.table[self.current]["blocks"].append(self.stack)
                self.stack = []
            elif isinstance(node, grammar.ElseStatement):
                self.table[self.current]["blocks"].append(self.stack)
                self.stack = []
            elif isinstance(node, grammar.LabelDeclaration):
                self.stack.insert(0, node.ir())
                self.table[self.current]["blocks"].append(self.stack)
                self.stack = []
            else:
                i = node.ir()
                if i is not None and not i.isdigit():
                    self.stack.append(i)

    def print(self):
        """Print the intermediate representation as a string."""

        for i in self.ir:
            print(i)
