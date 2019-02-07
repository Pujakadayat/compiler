import parser.classes as classes
import tokens as tokenTypes


def Program(tokens):
    """
    Grammar rule:
        Program -> FunctionDeclaration
    """
    if len(tokens) != 1:
        return None

    if isinstance(tokens[0], classes.FunctionDeclaration):
        return classes.Program(tokens[0])


def FunctionDeclaration(tokens):
    """
    Grammar rule:
        FunctionDeclaration -> TypeSpecifier ID () ReturnStatement
    """

    if len(tokens) != 7:
        return None

    returnType = tokens[0]
    if not isinstance(returnType, classes.TypeSpecifier):
        return None

    id = tokens[1]
    if not isinstance(id, classes.IDENTIFIER):
        return None

    if tokens[2].kind != tokenTypes.openParen:
        return None

    if tokens[3].kind != tokenTypes.closeParen:
        return None

    if tokens[4].kind != tokenTypes.openCurly:
        return None

    returnStatement = tokens[5]
    if not isinstance(returnStatement, classes.ReturnStatement):
        return None

    if tokens[6].kind != tokenTypes.closeCurly:
        return None

    return classes.FunctionDeclaration(returnType, id, None, returnStatement)


def TypeSpecifier(tokens):
    if len(tokens) != 1:
        return None

    token = tokens[0]

    if isinstance(token, classes.Node):
        return None

    if token.kind == tokenTypes.int:
        return classes.TypeSpecifier(tokenTypes.int)

    return None


def ReturnStatement(tokens):
    """
    Grammar rule:
        ReturnStatement -> return NUMCONST;
    """

    if len(tokens) != 3:
        return None

    if (
        isinstance(tokens[0], tokenTypes.Token)
        and tokens[0].kind != tokenTypes.returnKeyword
    ):
        return None

    # found 'return'

    if not isinstance(tokens[1], classes.NUMCONST):
        return None

    # found 'return 0'

    if not isinstance(tokens[2], tokenTypes.Token):
        return None

    if tokens[2].kind != tokenTypes.semicolon:
        return None

    # found 'return 0;'

    return classes.ReturnStatement(999999)


def NUMCONST(tokens):
    if len(tokens) != 1:
        return None

    token = tokens[0]
    if isinstance(token, classes.Node):
        return None

    if token.kind != tokenTypes.number:
        return None

    return classes.NUMCONST(token.content)


def IDENTIFIER(tokens):
    if len(tokens) != 1:
        return None

    token = tokens[0]

    if isinstance(token, classes.Node):
        return None

    if token.kind != tokenTypes.identifier:
        return None

    return classes.IDENTIFIER(token.content)


rules = [
    Program,
    FunctionDeclaration,
    TypeSpecifier,
    ReturnStatement,
    NUMCONST,
    IDENTIFIER,
]
