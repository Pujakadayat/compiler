class TokenList:
    """
    Represents a list of Tokens.
    """

    def __init__(self, tokenList=None):
        self.index = 0

        if tokenList:
            self.tokenList = tokenList
        else:
            self.tokenList = []

    def append(self, tokens):
        if isinstance(tokens, TokenList):
            self.tokenList += tokens.tokenList
        elif type(tokens) is list and len(tokens) > 1:
            self.tokenList += tokens
        else:
            self.tokenList.append(tokens)

    def get(self, index=None):
        if index:
            return self.tokenList[index]
        else:
            return self.tokenList[self.index]

    def peek(self):
        return self.tokenList[self.index + 1]

    def shift(self):
        # Remove the first item from the list and return it
        return self.tokenList.pop(0)

    def pop(self):
        # Remove the last item from the list and return it
        return self.tokenList.pop()

    def next(self):
        if self.index == len(self.tokenList) - 1:
            raise IndexError("Already at the end of the TokenList")

        self.index += 1
        return self.get()

    def previous(self):
        if self.index <= 0:
            raise IndexError("Already at the beginning of the TokenList")

        self.index -= 1
        return self.get()

    def print(self):
        text = []
        for token in self.tokenList:
            text.append(f"<{token.text}, {token.name}>")
        return str(text)

    def __repr__(self):
        return self.print()

    def __len__(self):
        return len(self.tokenList)


class Token:
    """
    A single token.

    Atrributes:
        type: TokenType that this token is an instance of
        content: Literal C string representation of this token
    """

    def __init__(self, type, text=""):
        self.type = type
        self.name = type.name

        if text:
            # You can pass a text value along with the token
            self.text = text
        else:
            # Otherwise we just use the standard string representation for this kind
            self.text = str(self.type)

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text


class TokenType:
    """
    A known token type (return, int, sizeof, etc...)

    Attributes:
        text: Literal C string representation of this token type
        type: Classification (symbols or keywords) of the token type
    """

    def __init__(self, name="", text="", type=[]):
        self.name = name
        self.text = text
        # self.name = name
        type.append(self)

        # Sort the list of this TokenType
        # NOTE: This is because we want to match longest matching tokens first.
        type.sort(key=lambda t: -len(t.text))

    def __str__(self):
        return self.text

    def __repr__(self):
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
identifiers = []

# ========
# Variable
# ========

identifier = TokenType("IDENTIFIER", identifiers)
number = TokenType("NUMBER")
string = TokenType("STRING")
character = TokenType("CHARACTER")
filename = TokenType("FILENAME")

# =======
# Symbols
# =======

# Blocks
openParen = TokenType("symbol", "(", symbols)
closeParen = TokenType("symbol", ")", symbols)
openCurly = TokenType("symbol", "{", symbols)
closeCurly = TokenType("symbol", "}", symbols)
openSquare = TokenType("symbol", "[", symbols)
closeSquare = TokenType("symbol", "]", symbols)

# Unary operations
ampersand = TokenType("symbol", "&", symbols)
pipe = TokenType("symbol", "|", symbols)
xor = TokenType("symbol", "^", symbols)
complement = TokenType("symbol", "~", symbols)

# Equality
lt = TokenType("symbol", "<", symbols)
gt = TokenType("symbol", ">", symbols)
ltoe = TokenType("symbol", "<=", symbols)
gtoe = TokenType("symbol", ">=", symbols)
doubleEquals = TokenType("symbol", "==", symbols)
notEquals = TokenType("symbol", "!=", symbols)

# Assignment
equals = TokenType("symbol", "=", symbols)
plusEquals = TokenType("symbol", "+=", symbols)
minusEquals = TokenType("symbol", "-=", symbols)
starEquals = TokenType("symbol", "*=", symbols)
slashEquals = TokenType("symbol", "/=", symbols)
plusPlus = TokenType("symbol", "++", symbols)
minusMinus = TokenType("symbol", "--", symbols)

# Strings
doubleQuote = TokenType("symbol", '"', symbols)
singleQuote = TokenType("symbol", "'", symbols)

# Misc
comma = TokenType("symbol", ",", symbols)
period = TokenType("symbol", ".", symbols)
semicolon = TokenType("symbol", ";", symbols)
backSlash = TokenType("symbol", "\\", symbols)
arrow = TokenType("symbol", "->", symbols)
pound = TokenType("symbol", "#", symbols)


# =========
# Operators
# =========

# Sum operations
plus = TokenType("operator", "+", symbols)
minus = TokenType("operator", "-", symbols)

# Multiplication operations
star = TokenType("operator", "*", symbols)
slash = TokenType("operator", "/", symbols)
mod = TokenType("operator", "%", symbols)

# Boolean operations
boolAnd = TokenType("operator", "&&", symbols)
boolOr = TokenType("operator", "||", symbols)
boolNot = TokenType("operator", "!", symbols)
leftShift = TokenType("operator", "<<", symbols)
rightShift = TokenType("operator", ">>", symbols)

# ========
# Keywords
# ========

# Numbers

int = TokenType("keyword", "int", keywords)
long = TokenType("keyword", "int", keywords)
double = TokenType("keyword", "int", keywords)
char = TokenType("keyword", "char", keywords)
short = TokenType("keyword", "short", keywords)
signed = TokenType("keyword", "signed", keywords)
unsigned = TokenType("keyword", "unsigned", keywords)
float = TokenType("keyword", "float", keywords)

# Data types

struct = TokenType("keyword", "struct", keywords)
enum = TokenType("keyword", "enum", keywords)
union = TokenType("keyword", "union", keywords)
record = TokenType("keyword", "record", keywords)

# Flow control

ifKeyword = TokenType("keyword", "if", keywords)
elseKeyword = TokenType("keyword", "else", keywords)
whileKeyword = TokenType("keyword", "while", keywords)
forKeyword = TokenType("keyword", "for", keywords)
breakKeyword = TokenType("keyword", "break", keywords)
continueKeyword = TokenType("keyword", "continue", keywords)
returnKeyword = TokenType("keyword", "return", keywords)

# Boolean

true = TokenType("keyword", "true", keywords)
false = TokenType("keyword", "false", keywords)

# Misc

static = TokenType("keyword", "static", keywords)
sizeof = TokenType("keyword", "sizeof", keywords)
typedef = TokenType("keyword", "typedef", keywords)
const = TokenType("keyword", "const", keywords)
extern = TokenType("keyword", "extern", keywords)
auto = TokenType("keyword", "auto", keywords)
