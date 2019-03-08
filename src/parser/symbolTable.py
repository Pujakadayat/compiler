"""
Contains the Symbol Table class.
"""

import json
import src.parser.grammar as grammar


class SymbolTable:
    """Symbol Table that represents all variables and their scopes in the program."""

    def __init__(self):
        self.table = {}
        self.table["name"] = "global"
        self.table["variables"] = []
        self.current = self.table

    def startScope(self, name):
        """Initialize a new scope."""

        # Add the new scope dict
        self.current[name] = {}
        self.current[name]["name"] = name

        # Initialize the dict with a .. and variables entry
        self.current[name][".."] = self.current
        self.current[name]["variables"] = []

        # Update the current pointer
        self.current = self.current[name]

    def declareVariable(self, name):
        """Declare a new variable in the current scope."""

        # TODO: add type to variable declaration
        # Append the variable to the current scope's variable list
        self.current["variables"].append(name)

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

    def print(self, t=None, level=0):
        """Pretty print the symbol table."""

        print("⚭ Symbol Table: ")
        print(self.table)
        print("")


def buildSymbolTable(parseTree):
    """Given the parse tree, build a symbol table."""

    st = SymbolTable()

    visitChildren(parseTree[0], st)

    st.endScope()

    st.print()
    return st


def visitChildren(node, st):
    """Visit each node of the parse tree."""

    if hasattr(node, "children"):
        updateSymbolTable(node, st)
        for child in node.children:
            visitChildren(child, st)
    elif isinstance(node, list):
        for child in node:
            visitChildren(child, st)

def updateSymbolTable(node, st):
    """Check if symbol table should be updated based on node."""

    if isinstance(node, grammar.FunctionDeclaration):
        st.startScope(node.name)
    elif isinstance(node, grammar.VariableDeclaration):
        st.declareVariable(node.name)
