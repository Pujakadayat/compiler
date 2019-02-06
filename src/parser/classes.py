class Program:
    def __init__(self, declarationList):
        # Declarations is a DeclarationList instance
        self.declarations = declarationList


class DeclarationList:
    def __init__(self, list=[]):
        # List contains a Python list of Declaration instances
        self.list = list


class Declaration:
    def __init__(self, type):
        # This is really just a general class to be extended
        pass


class VariableDeclaration(Declaration):
    def __init__(self, type, list):
        # Type is a TypeSpecifier instance, list is a variableDeclarationList instance
        self.type = type
        self.list = list


class FunctionDeclaration(Declaration):
    def __init__(self, type, ID, parameters, statement):
        self.type = type
        self.ID = ID
        self.parameters = parameters
        self.statement = statement


class Return:
    def __init__(self, value):
        self.value = value
