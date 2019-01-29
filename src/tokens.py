class Token:
    """
    A single token.

    Atrributes:
        type: TokenType that this token is an instance of
        content: Literal C string representation of this token
    """

    def __init__(self, type, text=""):
        self.type = type
        self.text = text

    def __str__(self):
        return self.text


class TokenType:
    """
    A known token type (return, int, sizeof, etc...)

    Attributes:
        text: Literal C string representation of this token type
        type: Classification (symbols or keywords) of the token type
    """

    def __init__(self, text="", type=[]):
        self.text = text
        type.append(self)

    def __str__(self):
        return self.text


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

identifiers = []
number = TokenType()
string = TokenType()
character = TokenType()

# =======
# Symbols
# =======

# Blocks
openParen = TokenType("(", symbols)
closeParen = TokenType(")", symbols)
openCurly = TokenType("{", symbols)
closeCurly = TokenType("}", symbols)
openSquare = TokenType("[", symbols)
closeSquare = TokenType("]", symbols)

# Sum operations
plus = TokenType("+", symbols)
minus = TokenType("-", symbols)

# Multiplication operations
star = TokenType("*", symbols)
slash = TokenType("/", symbols)
mod = TokenType("%", symbols)

# Unary operations
ampersand = TokenType("&", symbols)
pipe = TokenType("|", symbols)
xor = TokenType("^", symbols)
complement = TokenType("~", symbols)

# Boolean operations
boolAnd = TokenType("&&", symbols)
boolOr = TokenType("||", symbols)
boolNot = TokenType("!", symbols)
leftShift = TokenType("<<", symbols)
rightShift = TokenType(">>", symbols)

# Equality
lt = TokenType("<", symbols)
gt = TokenType(">", symbols)
ltoe = TokenType("<=", symbols)
gtoe = TokenType(">=", symbols)
doubleEquals = TokenType("==", symbols)
notEquals = TokenType("!=", symbols)

# Assignment
equals = TokenType("=", symbols)
plusEquals = TokenType("+=", symbols)
minusEquals = TokenType("-=", symbols)
starEquals = TokenType("*=", symbols)
slashEquals = TokenType("/=", symbols)
plusPlus = TokenType("++", symbols)
minusMinus = TokenType("--", symbols)

# Strings
doubleQuote = TokenType('"', symbols)
singleQuote = TokenType("'", symbols)

# Misc
comma = TokenType(",", symbols)
period = TokenType(".", symbols)
semicolon = TokenType(";", symbols)
backSlash = TokenType("\\", symbols)
arrow = TokenType("->", symbols)

# ========
# Keywords
# ========

# Numbers

int = TokenType("int", keywords)
long = TokenType("int", keywords)
double = TokenType("int", keywords)
char = TokenType("char", keywords)
short = TokenType("short", keywords)
signed = TokenType("signed", keywords)
unsigned = TokenType("unsigned", keywords)
float = TokenType("float", keywords)

# Data types

struct = TokenType("struct", keywords)
enum = TokenType("enum", keywords)
union = TokenType("union", keywords)
record = TokenType("record", keywords)

# Flow control

ifKeyword = TokenType("if", keywords)
elseKeyword = TokenType("else", keywords)
whileKeyword = TokenType("while", keywords)
forKeyword = TokenType("for", keywords)
breakKeyword = TokenType("break", keywords)
continueKeyword = TokenType("continue", keywords)

# Boolean

true = TokenType("true", keywords)
false = TokenType("false", keywords)

# Misc

static = TokenType("static", keywords)
sizeof = TokenType("sizeof", keywords)
typedef = TokenType("typedef", keywords)
const = TokenType("const", keywords)
extern = TokenType("extern", keywords)
auto = TokenType("auto", keywords)
