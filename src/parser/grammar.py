import tokens as tokenTypes


class Node:
    def __init__(self):
        pass

    def prettyPrint(self, level):
        for i in range(level):
            print("| -- ", end=" ")
        print(self.__class__.__name__)
        self.next(level+1)

    def next(self, level):
        return None


class Program(Node):
    def __init__(self, declarationList):
        # Declarations is a DeclarationList instance
        self.declarations = declarationList

    def next(self, level):
        self.declarations.prettyPrint(level)

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

    def next(self, level):
        self.statement.prettyPrint(level)

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

    def next(self, level):
        self.value.prettyPrint(level)

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

        return ReturnStatement(tokens[1])


class NUMCONST(Node):
    def __init__(self, value):
        self.value = value

    def next(self, level):
        return None

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

## TODO: implement statement, expression, unaryop
class SIMPLEEXPRESSION(Node):
    def __init__(self, value):
        self.value = value

    def parse(tokens):
        #parse as regular int
        if len(tokens) != 1:
            return None
        #else convert to unaryop
        token = tokens[0]

        #return
        return SIMPLEEXPRESSION(token.content)




rules = [
    Program,
    FunctionDeclaration,
    TypeSpecifier,
    ReturnStatement,
    NUMCONST,
    IDENTIFIER,
]
