import re
import sys
import time
#import tokens as tokens
#from tokens import TokenList, Token, TokenType, symbols, keywords, identifiers

class Parser(object):
    def __init__(self, tokens):
        #holds tokens created from lexer
        self.tokens = tokens
        #maintains current index when looping
        self.token_index = 0

        def parse(self):
            #holds the token type generated
            #holds the value of the token: "plus"
            while self.token_index < len(self.tokens):
                token_type = self.tokens[self.token_index][0]
                token_value = self.tokens[self.token_index][1]

                print(token_type, token_value)
                #loop through next token
                self.token_index += 1
