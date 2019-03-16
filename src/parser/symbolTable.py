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

    def print(self, node=None, level=0):
        """Pretty print the symbol table."""

        if not node:
            node = self.table

        grammar.printPrefix(level)
        print(f"{node['name']}: {node['variables']}")

        for key in node:
            if key not in ["name", "variables", ".."]:
                self.print(node[key], level + 1)


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
                c = flattenTree(root.children[0], reducer, seen)

                root.children = [root.children[1]]

                if isinstance(c, list):
                    for i in c:
                        root.children.append(i)
                else:
                    root.children.append(c)

                return root

        if len(root.children) == 1:
            # This is a DecList that only has a Dec child, no recurse
            return root.children[0]
        else:
            # Save the sibling
            dec = root.children[1]

            # Recurse on the DecList
            children = flattenTree(root.children[0], reducer, seen)

            c = [dec]

            if isinstance(children, list):
                for i in children:
                    c.append(i)
            else:
                c.append(children)

            return c

    # Current node is not a DecList,
    # we just want to descend the parse tree
    if isinstance(root, list):
        for item in root:
            flattenTree(item, reducer, seen)

    # Current node is not a DecList,
    # but we will need to update it's children reference
    if hasattr(root, "children"):
        children = []
        for item in root.children:
            children.append(flattenTree(item, reducer, seen))

        if isinstance(children[0], list):
            children = children[0]

        root.children = children
        return root

    # Not a reducer node, not a list, not a "complex" node
    # Just return it to be appended as a child
    return root


def buildSymbolTable(parseTree):
    """Given the parse tree, build a symbol table."""

    # NOTE: declarations are returned in reverse order than which
    # they appear in the token list / source code.
    # Potential problem? Not sure.
    flattenTree(parseTree, reducer=grammar.DeclarationList)
    flattenTree(parseTree, reducer=grammar.StatementList)

    st = SymbolTable()
    visitChildren(parseTree[0], st)

    print("")
    st.print()
    print("")
    return st


def visitChildren(node, st, level=0):
    """Visit each node of the parse tree."""

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
    elif isinstance(node, grammar.VariableDeclaration):
        st.declareVariable(node.type, node.name)
