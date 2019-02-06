class Program:
    """
    Grammar rule:
        program -> declarationList
    """

    def __init__(self, declarationList):
        # Declarations is a DeclarationList instance
        self.declarations = declarationList


class DeclarationList:
    """
    Grammar rule:
        declarationList -> declarationList declaration | declaration
    """

    def __init__(self, list=[]):
        # List contains a Python list of Declaration instances
        self.list = list


class Declaration:
    """
    Grammar rule:
        declaration -> variableDeclaration | functionDeclaration
    """

    def __init__(self, type):
        # This is really just a general class to be extended
        pass


class VariableDeclaration(Declaration):
    """
    Extends Declaration class.

    Grammar rule:
        variableDeclaration -> typeSpecifier variableDeclarationList;
    """

    def __init__(self, type, list):
        # Type is a TypeSpecifier instance, list is a variableDeclarationList instance
        self.type = type
        self.list = list


class FunctionDeclaration(Declaration):
    """
    Extends Declaration class.

    Grammar rule:
        functionDeclaration -> typeSpecifier ID ( parameters ) compoundStatement
    """

    def __init__(self, type, ID, parameters, statement):
        self.type = type
        self.ID = ID
        self.parameters = parameters
        self.statement = statement


class Return:
    """
    Grammar rule:
        returnStatement -> return; | return expression;
    """

    def __init__(self, value):
        self.value = value
