import tokens as TokenTypes
import parser.classes as classes


def program(tokens):
    if len(tokens) != 1:
        return None

    if isinstance(tokens[0], classes.FunctionDeclaration):
        return Program(tokens[0])


def functionDeclaration(tokens):
    if len(tokens) != 6:
        return None

    returnType = tokens.get()
    if not isinstance(returnType, classes.TypeSpecifier):
        return None

    id = tokens.next()
    if not isistance(id, classes.Identifier):
        return None

    if tokens.next() != tokenTypes.openParen:
        return None

    if tokens.next() != tokenTypes.closeParen:
        return None

    parameters = tokens.next()
    if not isinstance(parameters, classes.Parameters):
        return None

    returnStatement = tokens.next()
    if not isinstance(returnStatement, classes.ReturnStatement):
        return None

    return classes.FunctionDeclaration(returnType, id, parameters, returnStatement)


grammar = [
    program,
    functionDeclaration,
    # returnStatement,
    # numConst,
    # parameters,
]
