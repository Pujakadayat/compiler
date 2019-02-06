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
        return Program(tokens[0])


def FunctionDeclaration(tokens):
    """
    Grammar rule:
        FunctionDeclaration -> TypeSpecifier ID () ReturnStatement
    """

    if len(tokens) != 6:
        return None

    returnType = tokens[0]
    if not isinstance(returnType, classes.TypeSpecifier):
        return None

    id = tokens[1]
    if not isinstance(id, classes.IDENTIFIER):
        return None

    if tokens[2] != tokenTypes.openParen:
        return None

    if tokens[3] != tokenTypes.closeParen:
        return None

    parameters = tokens[4]
    if not isinstance(parameters, classes.Parameters):
        return None

    returnStatement = tokens[5]
    if not isinstance(returnStatement, classes.ReturnStatement):
        return None

    return classes.FunctionDeclaration(returnType, id, parameters, returnStatement)


def TypeSpecifier(tokens):
    if len(tokens) != 1:
        return None

    token = tokens[0]
    if isinstance(token, tokenTypes.Token):
        if token.text == "int":
            return classes.TypeSpecifier(tokenTypes.int)
        elif token.text == "float":
            return classes.TypeSpecifier(tokenTypes.float)

    return None


def ReturnStatement(tokens):
    """
    Grammar rule:
        ReturnStatement -> return NUMCONST;
    """

    if len(tokens) != 3:
        return None

    if tokens[0] != tokenTypes.returnKeyword:
        return None

    value = tokens[1]
    if value != tokenTypes.number:
        return None

    if tokens[2] != tokenTypes.semicolon:
        return None

    return classes.ReturnStatement(value)


def NUMCONST(tokens):
    if len(tokens) != 1:
        return None

    token = tokens[0]
    if isinstance(token, tokenTypes.Token):
        if tokens[0].text.isdigit():
            return classes.NUMCONST(tokens[0])


rules = [Program, FunctionDeclaration, TypeSpecifier, ReturnStatement, NUMCONST]
