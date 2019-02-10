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
        #return self.rep if self.rep else self.content
        return "<%s, %s>"%(self.content, self.kind.desc())


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
plus = TokenType("+", symbols, description="")
minus = TokenType("-", symbols, description="")

# Multiplication operations
star = TokenType("*", symbols, description="")
slash = TokenType("/", symbols, description="")
mod = TokenType("%", symbols, description="")

# Boolean operations
boolAnd = TokenType("&&", symbols, description="")
boolOr = TokenType("||", symbols, description="")
boolNot = TokenType("!", symbols, description="")
leftShift = TokenType("<<", symbols, description="")
rightShift = TokenType(">>", symbols, description="")

# ========
# Keywords
# ========

# Numbers

int = TokenType("int", keywords, description="")
long = TokenType("int", keywords, description="")
double = TokenType("int", keywords, description="")
char = TokenType("char", keywords, description="")
short = TokenType("short", keywords, description="")
signed = TokenType("signed", keywords, description="")
unsigned = TokenType("unsigned", keywords, description="")
float = TokenType("float", keywords, description="")

# Data types

struct = TokenType("struct", keywords, description="")
enum = TokenType("enum", keywords, description="")
union = TokenType("union", keywords, description="")
record = TokenType("record", keywords, description="")

# Flow control

ifKeyword = TokenType("if", keywords, description="")
elseKeyword = TokenType("else", keywords, description="")
whileKeyword = TokenType("while", keywords, description="")
forKeyword = TokenType("for", keywords, description="")
breakKeyword = TokenType("break", keywords, description="")
continueKeyword = TokenType("continue", keywords, description="")
returnKeyword = TokenType("return", keywords, description="")

# Boolean

true = TokenType("true", keywords, description="")
false = TokenType("false", keywords, description="")

# Misc

static = TokenType("static", keywords, description="")
sizeof = TokenType("sizeof", keywords, description="")
typedef = TokenType("typedef", keywords, description="")
const = TokenType("const", keywords, description="")
extern = TokenType("extern", keywords, description="")
auto = TokenType("auto", keywords, description="")
