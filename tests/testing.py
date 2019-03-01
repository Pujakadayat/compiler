"""
Each test case has an accompanying class.
Each have methods such as: test_lexer, test_parser & test_symbolTable
"""

"""
Usage: python3 -m tests.testing
"""

import unittest
import src.main as main

class AssignmentTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/assignment.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/assignment.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

#    def test_symbolTable(self):
#        filename = "samples/assignment.c"
#        grammar = "grammars/main_grammar.txt"
#        flags = ["-"]

class BasicMathTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/basic_math.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/basic_math.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    #def test_symbolTable(self):
        #self.

class ExpressionTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/expression.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/expression.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    #def test_symbolTable(self):
        #self.

class FloatTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/float.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/float.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    #def test_symbolTable(self):
        #self.

class ForTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/for.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/for.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    #def test_symbolTable(self):
        #self.

class FunctionTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/function.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/function.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    #def test_symbolTable(self):
        #self.

class HelloWorldTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/hello_world.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/hello_world.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    #def test_symbolTable(self):
        #self.

class IfElseTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/if_else.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/if_else.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    #def test_symbolTable(self):
        #self.

class IfTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/if.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/if.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    #def test_symbolTable(self):
        #self.

class IncludeTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/include.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/include.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    #def test_symbolTable(self):
        #self.

class LineBreakTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/linebreak.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/linebreak.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    #def test_symbolTable(self):
        #self.

class MathTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/math.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/math.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    #def test_symbolTable(self):
        #self.

class MultiLineCommentTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/multi_line_comment.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/multi_line_comment.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    #def test_symbolTable(self):
        #self.

class PlainTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/plain.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/plain.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    #def test_symbolTable(self):
        #self.

class SingleLineCommentTestCase(unittest.TestCase):

    def test_lexer(self):
        filename = "samples/single_line_comment.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-s"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    def test_parser(self):
        filename = "samples/single_line_comment.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

    #def test_symbolTable(self):
        #self.

if __name__ == '__main__':
    unittest.main()
