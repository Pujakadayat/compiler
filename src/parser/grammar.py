# pylint: disable=missing-docstring

"""
Classes that represent grammar rules for our Parse Tree.
"""


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
    return None


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
        First, print the class name, then print all its children.

        This method is overriden at lower level nodes like ConstNum.
        """

        printPrefix(level)
        print(self.__class__.__name__)

        for child in self.children[0]:
            child.print(level + 1)


# Parse Tree Node Classes


class Program(Node):
    pass


class DeclarationList(Node):
    pass


class Declaration(Node):
    pass


class FunctionDeclaration(Declaration):
    def __init__(self, *children):
        self.children = children;
        self.name = children[0][1].value


class StatementList(Node):
    pass


class Statement(Node):
    pass


class ReturnStatement(Statement):
    pass


class VariableDeclaration(Declaration):
    def __init__(self, *children):
        self.children = children;
        self.name = children[0][1].value


# Assignments


class VariableAssignment(Declaration):
    pass


class IncrementAssignment(VariableAssignment):
    pass


class DecrementAssignment(VariableAssignment):
    pass


class PlusEqualAssignment(VariableAssignment):
    pass


class MinusEqualAssignment(VariableAssignment):
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


# Statements


class ForStatement(Statement):
    pass


class IncludeStatement(Statement):
    pass


class CallStatement(Statement):
    pass


class IfStatement(Statement):
    pass


class ElseStatement(Statement):
    pass


# A dictionary of all the parse tree nodes we recognize
# Key: string of the grammar rule
# Value: the associated class

nodes = {
    "program": Program,
    "declarationList": DeclarationList,
    "declaration": Declaration,
    "varDec": VariableDeclaration,
    "assignment": VariableAssignment,
    "incAssignment": IncrementAssignment,
    "decAssignemnt": DecrementAssignment,
    "incEqualAssignment": PlusEqualAssignment,
    "decEqualAssignment": MinusEqualAssignment,
    "functionDeclaration": FunctionDeclaration,
    "statementList": StatementList,
    "statement": Statement,
    "returnStatement": ReturnStatement,
    "forStatement": ForStatement,
    "includeStatement": IncludeStatement,
    "callStatement": CallStatement,
    "ifStatement": IfStatement,
    "elseStatement": ElseStatement,
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


class Filename(Node):
    """Filename node."""

    def __init__(self, value):
        self.value = value

    def print(self, level=0):
        printPrefix(level)
        print(f"{self.__class__.__name__}: {self.value}")


# A dictionary of all the terminal parse tree nodes we recognize
# Key: string of the grammar rule
# Value: the associated class

terminals = {
    "typeSpecifier": TypeSpecifier,
    "ID": Identifier,
    "constNum": ConstNum,
    "fileName": Filename,
}
