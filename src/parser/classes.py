class Program:
    def __init__(self, declarationList):
        # Declarations is a DeclarationList instance
        self.declarations = declarationList


class FunctionDeclaration:
    def __init__(self, type, ID, parameters, statement):
        self.type = type
        self.ID = ID
        self.parameters = parameters
        self.statement = statement


class TypeSpecifier:
    def __init__(self, type):
        self.type = type


class ReturnStatement:
    def __init__(self, value):
        self.value = value


class NUMCONST:
    def __init__(self, value):
        self.value = value

class IDENTIFIER:
    def __init__(self, value):
        self.value = value
