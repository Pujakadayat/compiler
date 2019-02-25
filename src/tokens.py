class Token:
    """
    A single token.

    Attributes:
        content: stores additional information if number/identifier/string
        rep: string representation of this token
    """

    def __init__(self, kind, content="", rep=""):
        self.kind = kind
        self.content = content if content else str(self.kind)
        self.rep = rep

    def __repr__(self):
        return self.content

    def __str__(self):
        # return self.rep if self.rep else self.content
        return "<%s, %s>" % (self.content, self.kind.desc())


class TokenType:
    """
    A known token type (return, int, sizeof, etc...)

    Attributes:
        rep: The representation of this token in text, if it exists (i.e. 'int')
        type: The list to add this TokenType to (i.e. 'symbols')
    """

    def __init__(self, rep="", type=[], description=""):
        self.rep = rep
        type.append(self)
        self.description = description

        # Sort the list of this TokenType
        # NOTE: This is because we want to match longest matching tokens first.
        type.sort(key=lambda t: -len(t.rep))

    def __str__(self):
        return self.rep

    def desc(self):
        return self.description


# Have to avoid the following Python keywords...
# False     class       finally     is          return
# None      continue    for         lambda      try
# True      def         from        nonlocal    while
# and       del         global      not         with
# as        elif        if          or          yield
# assert    else        import      pass
# break     except      in          raise

symbols = []
keywords = []

# ========
# Variable
# ========

identifier = TokenType(description="ID")
number = TokenType(description="constNum")
string = TokenType(description="str")
character = TokenType(description="char")
filename = TokenType(description="fileName")
eof = TokenType(description="endOfFile")

# =======
# Symbols
# =======

# Blocks
openParen = TokenType("(", symbols, description="openParen")
closeParen = TokenType(")", symbols, description="closeParen")
openCurly = TokenType("{", symbols, description="openCurly")
closeCurly = TokenType("}", symbols, description="closeCurly")
openSquare = TokenType("[", symbols, description="openSquare")
closeSquare = TokenType("]", symbols, description="closeSquare")

# Unary operations
ampersand = TokenType("&", symbols, description="ampersand")
pipe = TokenType("|", symbols, description="pipe")
xor = TokenType("^", symbols, description="carrot")
complement = TokenType("~", symbols, description="tilda")

# Equality
lt = TokenType("<", symbols, description="lessThan")
gt = TokenType(">", symbols, description="greaterThan")
ltoe = TokenType("<=", symbols, description="lessThanEqualTo")
gtoe = TokenType(">=", symbols, description="greaterThanEqualTo")
doubleEquals = TokenType("==", symbols, description="doubleEquals")
notEquals = TokenType("!=", symbols, description="notEquals")

# Assignment
equals = TokenType("=", symbols, description="equals")
plusEquals = TokenType("+=", symbols, description="plusEquals")
minusEquals = TokenType("-=", symbols, description="minusEquals")
starEquals = TokenType("*=", symbols, description="starEquals")
slashEquals = TokenType("/=", symbols, description="slashEquals")
plusPlus = TokenType("++", symbols, description="plusPlus")
minusMinus = TokenType("--", symbols, description="minusMinus")

# Strings
doubleQuote = TokenType('"', symbols, description="doubleQuote")
singleQuote = TokenType("'", symbols, description="singleQuote")

# Misc
comma = TokenType(",", symbols, description="comma")
period = TokenType(".", symbols, description="period")
semicolon = TokenType(";", symbols, description="semicolon")
backSlash = TokenType("\\", symbols, description="backSlash")
arrow = TokenType("->", symbols, description="arrow")
pound = TokenType("#", symbols, description="pound")


# =========
# Operators
# =========

# Sum operations
plus = TokenType("+", symbols, description="addOp")
minus = TokenType("-", symbols, description="subtractOp")

# Multiplication operations
star = TokenType("*", symbols, description="multiplyOp")
slash = TokenType("/", symbols, description="divisionOp")
mod = TokenType("%", symbols, description="modOp")

# Boolean operations
boolAnd = TokenType("&&", symbols, description="logicalAnd")
boolOr = TokenType("||", symbols, description="logicalOr")
boolNot = TokenType("!", symbols, description="logicalNot")
leftShift = TokenType("<<", symbols, description="bitShiftLeft")
rightShift = TokenType(">>", symbols, description="bitShiftRight")

# ========
# Keywords
# ========

# Numbers

void = TokenType("void", keywords, description="typeSpecifier")
int = TokenType("int", keywords, description="typeSpecifier")
long = TokenType("long", keywords, description="typeSpecifier")
double = TokenType("double", keywords, description="typeSpecifier")
char = TokenType("char", keywords, description="typeSpecifier")
short = TokenType("short", keywords, description="typeSpecifier")
signed = TokenType("signed", keywords, description="typeSpecifier")
unsigned = TokenType("unsigned", keywords, description="typeSpecifier")
float = TokenType("float", keywords, description="typeSpecifier")

# Data types

struct = TokenType("struct", keywords, description="specialTypeSpecifier")
enum = TokenType("enum", keywords, description="specialTypeSpecifier")
union = TokenType("union", keywords, description="specialTypeSpecifier")
record = TokenType("record", keywords, description="specialTypeSpecifier")

# Flow control

ifKeyword = TokenType("if", keywords, description="ifKeyword")
elseKeyword = TokenType("else", keywords, description="elseKeyword")
whileKeyword = TokenType("while", keywords, description="whileKeyword")
forKeyword = TokenType("for", keywords, description="forKeyword")
breakKeyword = TokenType("break", keywords, description="breakKeyword")
continueKeyword = TokenType("continue", keywords, description="continueKeyword")
returnKeyword = TokenType("return", keywords, description="returnKeyword")

# Boolean

true = TokenType("true", keywords, description="trueKeyword")
false = TokenType("false", keywords, description="falseKeyword")

# Misc

static = TokenType("static", keywords, description="staticKeyword")
sizeof = TokenType("sizeof", keywords, description="sizeofKeyword")
typedef = TokenType("typedef", keywords, description="typedefKeyword")
const = TokenType("const", keywords, description="constKeyword")
extern = TokenType("extern", keywords, description="externKeyword")
auto = TokenType("auto", keywords, description="autoKeyword")
