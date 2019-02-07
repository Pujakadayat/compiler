class Node:
    def __init__(self):
        pass


class Program(Node):
    def __init__(self, declarationList):
        # Declarations is a DeclarationList instance
        self.declarations = declarationList


class FunctionDeclaration(Node):
    def __init__(self, type, ID, parameters, statement):
        self.type = type
        self.ID = ID
        self.parameters = parameters
        self.statement = statement


class TypeSpecifier(Node):
    def __init__(self, type):
        self.type = type


class ReturnStatement(Node):
    def __init__(self, value):
        self.value = value


class Parameters(Node):
    def __init__(self):
        pass


class NUMCONST(Node):
    def __init__(self, value):
        self.value = value


class IDENTIFIER(Node):
    def __init__(self, value):
        self.value = value
