import tokens as tokenTypes


class Node:
    def __init__(self):
        pass


class Program(Node):
    def __init__(self, declarationList):
        # Declarations is a DeclarationList instance
        self.declarations = declarationList

    def __str__(self):
        return "member of Test"

    def parse(tokens):
        if len(tokens) != 1:
            return None

        if isinstance(tokens[0], FunctionDeclaration):
            return Program(tokens[0])


class FunctionDeclaration(Node):
    def __init__(self, type, ID, parameters, statement):
        self.type = type
        self.ID = ID
        self.parameters = parameters
        self.statement = statement

    def parse(tokens):
        if len(tokens) != 7:
            return None

        returnType = tokens[0]
        if not isinstance(returnType, TypeSpecifier):
            return None

        id = tokens[1]
        if not isinstance(id, IDENTIFIER):
            return None

        if tokens[2].kind != tokenTypes.openParen:
            return None

        if tokens[3].kind != tokenTypes.closeParen:
            return None

        if tokens[4].kind != tokenTypes.openCurly:
            return None

        returnStatement = tokens[5]
        if not isinstance(returnStatement, ReturnStatement):
            return None

        if tokens[6].kind != tokenTypes.closeCurly:
            return None

        return FunctionDeclaration(returnType, id, None, returnStatement)


class TypeSpecifier(Node):
    def __init__(self, type):
        self.type = type

    def parse(tokens):
        if len(tokens) != 1:
            return None

        token = tokens[0]

        if isinstance(token, Node):
            return None

        if token.kind == tokenTypes.int:
            return TypeSpecifier(tokenTypes.int)

        return None


class ReturnStatement(Node):
    def __init__(self, value):
        self.value = value

    def parse(tokens):
        if len(tokens) != 3:
            return None

        if (
            isinstance(tokens[0], tokenTypes.Token)
            and tokens[0].kind != tokenTypes.returnKeyword
        ):
            return None

        if not isinstance(tokens[1], NUMCONST):
            return None

        if not isinstance(tokens[2], tokenTypes.Token):
            return None

        if tokens[2].kind != tokenTypes.semicolon:
            return None

        return ReturnStatement(999999)


class NUMCONST(Node):
    def __init__(self, value):
        self.value = value

    def parse(tokens):
        if len(tokens) != 1:
            return None

        token = tokens[0]
        if isinstance(token, Node):
            return None

        if token.kind != tokenTypes.number:
            return None

        return NUMCONST(token.content)


class IDENTIFIER(Node):
    def __init__(self, value):
        self.value = value

    def parse(tokens):
        if len(tokens) != 1:
            return None

        token = tokens[0]

        if isinstance(token, Node):
            return None

        if token.kind != tokenTypes.identifier:
            return None

        return IDENTIFIER(token.content)


rules = [
    Program,
    FunctionDeclaration,
    TypeSpecifier,
    ReturnStatement,
    NUMCONST,
    IDENTIFIER,
]
