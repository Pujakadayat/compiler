# pylint: disable=missing-docstring

"""
Classes that represent grammar rules for our Parse Tree.
"""

count = {"none": 0}


def unique(prefix=None):
    """Generate a new, unique variable name with optional prefix."""

    if prefix:
        if prefix not in count:
            count[prefix] = 0
        count[prefix] += 1
        return f"{prefix}{count[prefix]}"

    count["none"] += 1
    return f"r{count['none']}"


def generateIr(parseTree):
    """Generate an intermediate representation from a parse tree."""

    ir = []
    visitChildren(parseTree, ir)
    return ir


def visitChildren(node, ir):
    """Visit each node of the parse tree."""

    if isinstance(node, FunctionDeclaration):
        ir.append(node.ir())

    if hasattr(node, "children"):
        for child in node.children:
            visitChildren(child, ir)
    elif isinstance(node, list):
        for child in node:
            visitChildren(child, ir)

    if not isinstance(node, list):
        if not isinstance(node, FunctionDeclaration):
            i = node.ir()
            if i is not None and not i.isdigit():
                ir.append(i)


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
        self.type = children[0].value
        self.name = children[1].value

    def ir(self):
        return f".{self.name} ()"


class StatementList(Node):
    pass


class Statement(Node):
    pass


class ReturnStatement(Node):
    def ir(self):
        expr = self.children[0]
        return f"ret {expr.children[0].value}"


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

        return f"{self.name} = null"


# Assignments


class VariableAssignment(Node):
    def __init__(self, *children):
        self.children = children
        self.name = children[0][0].value

    def ir(self):
        recent = count["none"]
        return f"{self.name} = r{recent}"


class IncrementAssignment(Node):
    def __init__(self, *children):
        self.children = children
        self.name = children[0][0].value

    def ir(self):
        return f"{self.name} = {self.name} + 1"


class DecrementAssignment(Node):
    def __init__(self, *children):
        self.children = children
        self.name = children[0][0].value

    def ir(self):
        return f"{self.name} = {self.name} - 1"


class PlusEqualAssignment(Node):
    def __init__(self, *children):
        self.children = children


class MinusEqualAssignment(Node):
    pass


# Expressions


class Expression(Node):
    pass


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
    pass


class BooleanOr(Node):
    pass


class LTOEExpression(Node):
    pass


class GTOEExpression(Node):
    pass


class LTExpression(Node):
    pass


class GTExpression(Node):
    pass


class NotEqualExpression(Node):
    pass


class EqualExpression(Node):
    pass


# Statements


class ForStatement(Node):
    pass


class IncludeStatement(Node):
    pass


class CallStatement(Node):
    pass


class IfStatement(Node):
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


# A dictionary of all the terminal parse tree nodes we recognize
# Key: string of the grammar rule
# Value: the associated class

terminals = {
    "typeSpecifier": TypeSpecifier,
    "ID": Identifier,
    "constNum": ConstNum,
    "fileName": Filename,
    "str": String,
}
