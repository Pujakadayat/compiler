# pylint: disable=missing-docstring, attribute-defined-outside-init

"""
Classes that represent grammar rules for our Parse Tree.
"""

from src.util import count, unique


def parseToken(desc, content="", children=None):
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
        self.value = None

        if len(children) == 1:
            self.children = children[0]
        else:
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

        if isinstance(self.children, list):
            for child in self.children:
                child.print(level + 1)
        else:
            for child in self.children[0]:
                child.print(level + 1)

    # pylint: disable=no-self-use
    def ir(self):
        return None

    def prepare(self):
        return None

    # pylint: enable=no-self-use

    def visit(self):
        if hasattr(self, "children"):
            for child in self.children:
                child.visit()

        self.prepare()


# Parse Tree Node Classes


class Program(Node):
    pass


class DeclarationList(Node):
    pass


class Declaration(Node):
    pass


class FunctionDeclaration(Node):
    def __init__(self, children):
        self.children = children
        self.type = self.children[0].value
        self.name = self.children[1].value
        self.arguments = self.children[2]

    def ir(self):
        return f".{self.name} ({self.arguments.value})"


class Arguments(Node):
    def prepare(self):
        s = []
        for i in self.children:
            s.append(i.name)

        self.value = ", ".join(s)


class Argument(Node):
    def __init__(self, children):
        self.children = children
        self.type = children[0].value
        if len(children) > 1:
            self.name = children[1].value
        # added this for the case "main(void)"
        else:
            self.name = "None"


class Parameters(Node):
    def prepare(self):
        s = []
        for i in self.children:
            s.append(i.value)

        self.value = ", ".join(s)


class Parameter(Node):
    def __init__(self, children):
        self.children = children
        self.value = children[0].value


class StatementList(Node):
    pass


class Statement(Node):
    pass


class StatementListNew(Node):
    pass


class StatementNew(Node):
    pass


class ReturnStatement(Node):
    def prepare(self):
        self.expr = self.children[0]

    def ir(self):
        return f"ret {self.expr.value}"


class VariableDeclaration(Node):
    def __init__(self, children):
        self.children = children
        self.type = children[0].value
        self.name = children[1].value

        # If this VarDec is also assigned
        if len(self.children) == 3:
            self.expr = self.children[2]

    def ir(self):
        if len(self.children) == 3:
            return f"{self.name} = {self.expr.children[0].value}"

        return None


class LabelDeclaration(Node):
    def ir(self):
        self.value = self.children[0].value
        return f"label: {self.value}"


# Assignments


class VariableAssignment(Node):
    def __init__(self, children):
        self.children = children
        self.name = children[0].name

    def ir(self):
        recent = count["none"]
        return f"{self.name} = r{recent}"


class IncrementAssignment(Node):
    def __init__(self, children):
        self.children = children
        self.name = self.children[0].value

    def ir(self):
        self.value = unique()
        return f"{self.value} = {self.name} + 1"


class DecrementAssignment(Node):
    def __init__(self, children):
        self.children = children
        self.name = self.children[0].value

    def ir(self):
        self.value = unique()
        return f"{self.value} = {self.name} - 1"


class PlusEqualAssignment(Node):
    def __init__(self, children):
        self.children = children
        self.name = self.children[0].value
        self.expr = self.children[1]

    def ir(self):
        self.value = unique()
        return f"{self.value} = {self.name} + {self.expr.value}"


class MinusEqualAssignment(Node):
    def __init__(self, children):
        self.children = children
        self.name = self.children[0].value
        self.expr = self.children[1]

    def ir(self):
        self.value = unique()
        return f"{self.value} = {self.name} - {self.expr.value}"


class CallAssignment(Node):
    def __init__(self, children):
        self.children = children
        self.name = self.children[0].value
        self.expr = self.children[1]

    def ir(self):
        self.value = unique()
        return f"{self.value} = call {self.name} - {self.expr.value}"


class ExpressionAssignment(Node):
    def __init__(self, children):
        self.children = children
        self.name = self.children[0].value
        self.expr = self.children[1]

    def ir(self):
        self.value = unique()
        return f"{self.value} = {self.expr.value}"


# Expressions


class Expression(Node):
    def ir(self):
        self.value = self.children[0].value


class NestedExpression(Node):
    def ir(self):
        self.value = self.children[0].value


class AdditionExpression(Node):
    def ir(self):
        self.value = unique()
        return f"{self.value} = {self.children[0].value} + {self.children[1].value}"


class SubtractionExpression(Node):
    def ir(self):
        self.value = unique()
        return f"{self.value} = {self.children[0].value} - {self.children[1].value}"


class MultiplicationExpression(Node):
    def ir(self):
        self.value = unique()
        return f"{self.value} = {self.children[0].value} * {self.children[1].value}"


class DivisionExpression(Node):
    def ir(self):
        self.value = unique()
        return f"{self.value} = {self.children[0].value} / {self.children[1].value}"


class ModulusExpression(Node):
    def ir(self):
        self.value = unique()
        return f"{self.value} = {self.children[0].value} % {self.children[1].value}"


class BooleanAnd(Node):
    def ir(self):
        self.value = unique()
        return f"{self.value} = {self.children[0].value} && {self.children[1].value}"


class BooleanOr(Node):
    def ir(self):
        self.value = unique()
        return f"{self.value} = {self.children[0].value} || {self.children[1].value}"


class BooleanNot(Node):
    def ir(self):
        self.value = unique()
        return f"{self.value} = !{self.children[0].value}"


class ComparisonExpression(Node):
    def prepare(self):
        self.value = unique()
        self.a = self.children[0].value
        self.b = self.children[1].value


class LTOEExpression(ComparisonExpression):
    def ir(self):
        return f"{self.value} = {self.a} <= {self.b}"


class GTOEExpression(ComparisonExpression):
    def ir(self):
        return f"{self.value} = {self.a} >= {self.b}"


class LTExpression(ComparisonExpression):
    def ir(self):
        return f"{self.value} = {self.a} < {self.b}"


class GTExpression(ComparisonExpression):
    def ir(self):
        return f"{self.value} = {self.a} > {self.b}"


class NotEqualExpression(ComparisonExpression):
    def ir(self):
        return f"{self.value} = {self.a} != {self.b}"


class EqualExpression(ComparisonExpression):
    def ir(self):
        return f"{self.value} = {self.a} == {self.b}"


# Statements


class ForStatement(Node):
    pass


class WhileStatement(Node):
    def ir(self):
        return f"while {self.children[0].ir()} is true"


class WhileCondition(Node):
    pass


class IncludeStatement(Node):
    pass


class CallStatement(Node):
    def __init__(self, children):
        self.children = children
        self.name = self.children[0].value
        self.parameters = self.children[1]

    def ir(self):
        self.value = unique()
        return f"{self.value} = call {self.name} ({self.parameters.value})"


class GotoStatement(Node):
    def ir(self):
        self.value = self.children[0].value
        return f"goto {self.value}"


class IfStatement(Node):
    def __init__(self, children):
        self.children = children
        self.condition = self.children[0]
        self.body = self.children[1]


class Condition(Node):
    pass


class ElseStatement(Node):
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
    "exprAssignment": ExpressionAssignment,
    "callAssignment": CallAssignment,
    "incAssignment": IncrementAssignment,
    "decAssignment": DecrementAssignment,
    "incEqualAssignment": PlusEqualAssignment,
    "decEqualAssignment": MinusEqualAssignment,
    "functionDeclaration": FunctionDeclaration,
    "labelDeclaration": LabelDeclaration,
    "argList": Arguments,
    "arg": Argument,
    "statementList": StatementList,
    "statementListNew": StatementListNew,
    "statement": Statement,
    "stateemntNew": StatementNew,
    "returnStatement": ReturnStatement,
    "forStatement": ForStatement,
    "whileStatement": WhileStatement,
    "whileCondition": WhileCondition,
    "includeStatement": IncludeStatement,
    "callStatement": CallStatement,
    "gotoStatement": GotoStatement,
    "paramList": Parameters,
    "param": Parameter,
    "ifStatement": IfStatement,
    "condition": Condition,
    "elseStatement": ElseStatement,
    "expression": Expression,
    "nestedExpr": NestedExpression,
    "addExpr": AdditionExpression,
    "subExpr": SubtractionExpression,
    "multExpr": MultiplicationExpression,
    "divExpr": DivisionExpression,
    "modExpr": ModulusExpression,
    "boolAnd": BooleanAnd,
    "boolOr": BooleanOr,
    "boolNot": BooleanNot,
    "lteExpr": LTOEExpression,
    "gteExpr": GTOEExpression,
    "ltExpr": LTExpression,
    "gtExpr": GTExpression,
    "neExpr": NotEqualExpression,
    "eExpr": EqualExpression,
}

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


class String(Node):
    """String node."""

    def __init__(self, value):
        self.value = value

    def print(self, level=0):
        printPrefix(level)
        print(f"{self.__class__.__name__}: {self.value}")


class Label(Node):
    """Label node."""

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
    "str": String,
    "label": Label,
}
