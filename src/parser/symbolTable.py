"""
Contains the Symbol Table class.
"""

import src.parser.grammar as grammar


class SymbolTable:
    """Symbol Table that represents all variables and their scopes in the program."""

    def __init__(self):
        self.table = {}
        self.table["name"] = "global"
        self.table["variables"] = []
        self.current = self.table
        self.level = 0

    def startScope(self, name, level):
        """Initialize a new scope."""

        # Add the new scope dict
        self.current[name] = {}
        self.current[name]["name"] = name

        # Initialize the dict with a .. and variables entry
        self.current[name][".."] = self.current
        self.current[name]["variables"] = []

        # Update the current pointer
        self.current = self.current[name]

        # Set the current level of scope
        self.level = level

    def declareVariable(self, t, name):
        """Declare a new variable in the current scope."""

        # TODO: add type to variable declaration
        # Append the variable to the current scope's variable list
        self.current["variables"].append((t, name))

    def endScope(self):
        """Finalize a scope and return it's parent scope."""

        # Go back up one scope
        if ".." in self.current:
            self.current = self.current[".."]

    def find(self, name):
        """Find the specified variable in the Symbol Table, starting from the current scope."""

        c = self.current

        # Search the global table first
        if c == self.table:
            if name in c["variables"]:
                return self.table["name"]

            return None

            # Search up the tree from our current scope
            # as long as there is a parent
        while ".." in c:
            if name in c["variables"]:
                return c["name"]

            c = c[".."]

        # Not found in any scope, return False
        return None

    def print(self):
        """Pretty print the symbol table."""

        print("⚭ Symbol Table: ")
        print(self.table)
        print("")

def flattenTree(root, reducer, seen=False):
    """
    Collapse recursive rules to have a single parent.
    The grammar rule to collapse should be specified in reducer.
    i.e. DeclarationList or StatementList.
    """

    if isinstance(root, reducer):
        if not seen:
            seen = True

            if len(root.children) == 1:
                return root
            else:
                root.children = [root.children[1], flattenTree(root.children[0], reducer, seen)]
                return root

        if len(root.children) == 1:
            # This is a DecList that only has a Dec child, no recurse
            return root.children[0]
        else:
            # Save the sibling
            dec = root.children[1]

            # Recurse on the DecList
            children = flattenTree(root.children[0], reducer, seen)

            return [dec, children]

    # Current node is not a DecList,
    # we just want to descend the parse tree
    if isinstance(root, list):
        for item in root:
            flattenTree(item, reducer, seen)

    if hasattr(root, "children"):
        children = []
        for item in root.children:
            children.append(flattenTree(item, reducer, seen))
        root.children = children
        return root


    return item


def buildSymbolTable(pt):
    """Given the parse tree, build a symbol table."""

    parseTree = pt.copy()

    print("------")

    tmp = flattenTree(parseTree, reducer=grammar.DeclarationList)
    print(tmp)      # program
    print(tmp.children) # [decList]
    print(tmp.children[0].children) # [dec, [dec, dec]]

    print("------")

    # st = SymbolTable()

    # # TODO: flatten the symbol table
    # # building the symbol table will not work until that happens
    # visitChildren(parseTree[0], st)

    # st.endScope()

    # st.print()
    # return st


def visitChildren(node, st, level=0):
    """Visit each node of the parse tree."""

    print(f"Visiting node: {node} at level {level}")

    if hasattr(node, "children"):
        updateSymbolTable(node, st, level)
        for child in node.children:
            visitChildren(child, st, level + 1)
    elif isinstance(node, list):
        for child in node:
            visitChildren(child, st, level + 1)


def updateSymbolTable(node, st, level=0):
    """Check if symbol table should be updated based on node."""

    if isinstance(node, grammar.FunctionDeclaration):
        if st.level == level:
            st.endScope()
        st.startScope(node.name, level)
        print(f"starting scope with level {level}")
    elif isinstance(node, grammar.VariableDeclaration):
        st.declareVariable(node.type, node.name)
