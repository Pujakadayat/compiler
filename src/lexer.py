import tokens
from tokens import Token, TokenType, symbols, keywords, identifiers


def tokenize(code):
    # Big array of parsed Tokens
    # NOTE: this is a list of Token instances, not just strings
    tokens = []

    lines = code.splitlines()
    # TODO: handle multiple escaped lines using \
    # lines = combineEscapedLines(lines)

    for line in lines:
        try:
            # Get the tokens of the current line and add to the big list
            lineTokens = tokenizeLine(line)
            tokens += lineTokens
        except Exception as err:
            print(err)
            sys.exit(2)


def tokenizeLine(line):
    """Parse a line into tokens"""
    tokens = []

    isInclude = False
    isComment = False

    # We parse characters in a "chunk" with a start and an end
    start = 0
    end = 0

    while end < len(line):
        symbol = matchSymbol(line, end)
        nextSymbol = matchSymbol(line, end + 1)

        # Order of searching:
        # 1. Symbols
        # 2. Keywords
        # 3. Identifiers
        # 4. Numbers

        # TODO: check if we are in an include statement
        # if isInclude:

        # If we are in a multi-line /* */ comment
        if isComment:
            # If the comment is ending
            if symbol == tokens.star and next == tokens.slash:
                isComment = False
                start = end + 2
                end = start
            else:
                start += 1
                end = start
            continue

        # If next two symbols begin a multi-line /* */ comment
        if symbol == tokens.star and next == tokens.slash:
            # Tokenize whatever we found up to this point
            isComment = True
            previousTokens = tokenizeChunk(line[start:end])
            tokens.append(previousTokens)
            continue

        # If next two tokens are //, skip this line and return
        if symbol == tokens.slash and nextSymbol == tokens.slash:
            break

        # If ending character of chunk is whitespace
        if line[end].isSpace():
            # Tokenize whatever we found up to this point, and skip whitespace
            previousTokens = tokenizeChunk(line[start:end])
            tokens.append(previousTokens)
            start = end + 1
            end = start

        # If we see a quote, tokenize the entire quoted value as one token
        if symbol in {tokens.doubleQuote, tokens.singleQuote}:
            if symbol == tokens.doubleQuote:
                delimeter = '"'
                kind = tokens.string
            elif symbol == tokens.singleQuote:
                delimeter = "'"
                kind = tokens.character

            # Get the token between the quotes and update our chunk end
            token, end = parseQuote(line, start, kind)
            tokens.append(token)

            start = end + 1
            end = start
            continue

        # If current symbol is another symbol
        if symbol is not None:
            # Tokenize whatever we found up to this point
            previousTokens = tokenizeChunk(line[start:end])
            tokens.append(previousTokens)

            # Append the next token
            tokens.append(Token(symbol.kind))
            continue

        # If none of the above cases have hit, we must increase our search
        # So we increment our chunk end to include an additional character
        end += 1

    # At this point we have parsed the entire line
    # Flush anything left in the chunk
    previousTokens = tokenizeChunk(line[start:end])
    tokens.append(previousTokens)

    # Finally return the list of tokens for this line
    return tokens


# def tokenizeChunk(text, start):
    # I will do this later...

def matchSymbol(text, start):
    """Check if a string matches a symbol"""
    for symbol in symbols:
        try:
            for i, c in enumerate(symbol.text):
                if text[start + i] != c:
                    break
                else:
                    return symbol
        except IndexError:
            pass


def matchKeyword(text):
    """Check if string matches a keyword"""
    for keyword in keywords:
        if keyword.text == text:
            return keyword


def matchIdentifier(text):
    """Check if string matches an identifier"""
    if re.match(r"[a-zA-Z][_a-zA-Z0-9]*$", text):
        return text


def matchNumber(text):
    """Check if string matches a number"""
    if text.isDigit():
        return text
