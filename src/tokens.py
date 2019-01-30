class Token:
    """
    A single token.

    Atrributes:
        type: TokenType that this token is an instance of
        content: Literal C string representation of this token
    """

    def __init__(self, type, text=""):
        self.type = type

        if text:
            # You can pass a text value along with the token
            self.text = text
        else:
            # Otherwise we just use the standard string representation for this kind
            self.text = str(self.type)

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

        # Sort the list of this TokenType
        # NOTE: This is because we want to match longest matching tokens first.
        type.sort(key=lambda t: -len(t.text))

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
operators = []
keywords = []

# ========
# Variable
# ========

identifiers = []
identifier = TokenType()
number = TokenType()
string = TokenType()
character = TokenType()
filename = TokenType()

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

# Unary operations
ampersand = TokenType("&", symbols)
pipe = TokenType("|", symbols)
xor = TokenType("^", symbols)
complement = TokenType("~", symbols)

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
pound = TokenType("#", symbols)


# =========
# Operators
# =========

# Sum operations
plus = TokenType("+", operators)
minus = TokenType("-", operators)

# Multiplication operations
star = TokenType("*", operators)
slash = TokenType("/", operators)
mod = TokenType("%", operators)

# Boolean operations
boolAnd = TokenType("&&", operators)
boolOr = TokenType("||", operators)
boolNot = TokenType("!", operators)
leftShift = TokenType("<<", operators)
rightShift = TokenType(">>", operators)

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
