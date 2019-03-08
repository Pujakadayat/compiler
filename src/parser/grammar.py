# pylint: disable=missing-docstring

"""
Classes that represent grammar rules for our Parse Tree.
"""

nodes = {}


def parseToken(desc, content="", children=[]):
    """Parse a token into the relevant class."""

    # Check if the node is a terminal
    if desc in terminals:
        return terminals[desc](content)

    # Check if the node exists
    if desc in nodes:
        return nodes[desc](children)

    # Did not match any of the known parse tree nodes.
    # Classify it as a "general"  node
    return GeneralNode(content, children)


def printPrefix(level):
    """Print a prefix level deep for pretty printing."""

    for _ in range(level):
        print("  ", end=" ")
    print("| - ", end=" ")


class Node:
    """General parse tree node class"""

    def __init__(self, *children):
        self.children = children

    def __str__(self):
        return self.__class__.__name__

    def print(self, level=0):
        """
        General node print method.
        First, print the class name, then print all it's children.

        This method is overriden at lower level nodes like NUMCONST.
        """

        printPrefix(level)
        print(self.__class__.__name__)

        for child in self.children[0]:
            child.print(level + 1)


# Parse Tree Node Classes


class Program(Node):
    pass


class FunctionDeclaration(Node):
    pass


class ReturnStatement(Node):
    pass


class VariableDeclaration(Node):
    pass


class VariableAssignment(Node):
    pass


# Expressions


class Expression(Node):
    pass


class AdditionExpression(Expression):
    pass


class SubtractionExpression(Expression):
    pass


class MultiplicationExpression(Expression):
    pass


class DivisionExpression(Expression):
    pass


class ModulusExpression(Expression):
    pass


class BooleanAnd(Expression):
    pass


class BooleanOr(Expression):
    pass


class LTOEExpression(Expression):
    pass


class GTOEExpression(Expression):
    pass


class LTExpression(Expression):
    pass


class GTExpression(Expression):
    pass


class NotEqualExpression(Expression):
    pass


class EqualExpression(Expression):
    pass


class ForStatement(Node):
    pass


class IncrementAssignment(VariableAssignment):
    pass


class DecrementAssignment(VariableAssignment):
    pass

class PlusEqualAssignment(VariableAssignment):
    pass

class MinusEqualAssignment(VariableAssignment):
    pass


# A dictionary of all the parse tree nodes we recognize
# Key: string of the grammar rule
# Value: the associated class

nodes = {
    "program": Program,
    "funcDec": FunctionDeclaration,
    "varDec": VariableDeclaration,
    "assignment": VariableAssignment,
    "incAssignment": IncrementAssignment,
    "decAssignemnt": DecrementAssignment,
    "incEqualAssignment": PlusEqualAssignment,
    "decEqualAssignment": MinusEqualAssignment,
    "returnStatement": ReturnStatement,
    "expression": Expression,
    "addExpr": AdditionExpression,
    "subExpr": SubtractionExpression,
    "multExpr": MultiplicationExpression,
    "divExpr": DivisionExpression,
    "modExpr": ModulusExpression,
    "boolAnd": BooleanAnd,
    "boolOr": BooleanOr,
    "lteExpr": LTOEExpression,
    "gteExpr": GTOEExpression,
    "ltExpr": LTExpression,
    "gtExpr": GTExpression,
    "neExpr": NotEqualExpression,
    "eExpr": EqualExpression,
    "forStatement": ForStatement
}

# General Node fallback


class GeneralNode(Node):
    """General node (fallback)."""

    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def print(self, level=0):
        # if len(self.children) == 0:
        #    printPrefix(level)
        #    print(self.value)
        # else:
        for child in self.children:
            child.print(level)


# Terminal Nodes


class TypeSpecifier(Node):
    """Type specifier node."""

    def __init__(self, value):
        self.value = value

    def print(self, level=0):
        printPrefix(level)
        print(f"{self.__class__.__name__}: {self.value}")


class ConstNum(Node):
    """Number constant node."""

    def __init__(self, value):
        self.value = value

    def print(self, level=0):
        printPrefix(level)
        print(f"{self.__class__.__name__}: {self.value}")


class Identifier(Node):
    """ID node."""

    def __init__(self, value):
        self.value = value

    def print(self, level=0):
        printPrefix(level)
        print(f"{self.__class__.__name__}: {self.value}")


terminals = {"typeSpecifier": TypeSpecifier, "ID": Identifier, "constNum": ConstNum}
