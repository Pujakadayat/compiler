"""
Each test case has an accompanying class.
Each have methods such as: test_lexer, test_parser & test_symbolTable
"""

"""
Usage: python3 -m testing.py
"""

import unittest
import src.main as main

class AssignmentTestCase(unittest.TestCase):

    def test_lexer(self):
        self.assertEqual("✨ Completed scanning!".main.run(), "✨ Completed scanning!")

    def test_islexer(self):
        self.assertTrue("✨ Completed scanning!".main.run())
        self.assertFalse("".main.run())

    def test_parser(self):
        filename = "samples/assignment.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)
"""
    def test_symbolTable(self):
        #self.

class BasicMathTestCase(unittest.TestCase):

    def test_lexer(self):
        #self.

    def test_parser(self):
        #self.

    def test_symbolTable(self):
        #self.

class ExpressionTestCase(unittest.TestCase):

    def test_lexer(self):
        #self.

    def test_parser(self):
        #self.

    def test_symbolTable(self):
        #self.

class FloatTestCase(unittest.TestCase):

    def test_lexer(self):
        #self.

    def test_parser(self):
        #self.

    def test_symbolTable(self):
        #self.

class ForTestCase(unittest.TestCase):

    def test_lexer(self):
        #self.

    def test_parser(self):
        #self.

    def test_symbolTable(self):
        #self.

class FunctionTestCase(unittest.TestCase):

    def test_lexer(self):
        #self.

    def test_parser(self):
        #self.

    def test_symbolTable(self):
        #self.

class HelloWorldTestCase(unittest.TestCase):

    def test_lexer(self):
        #self.

    def test_parser(self):
        #self.

    def test_symbolTable(self):
        #self.

class IfElseTestCase(unittest.TestCase):

    def test_lexer(self):
        #self.

    def test_parser(self):
        #self.

    def test_symbolTable(self):
        #self.

class IfTestCase(unittest.TestCase):

    def test_lexer(self):
        #self.

    def test_parser(self):
        #self.

    def test_symbolTable(self):
        #self.

class IncludeTestCase(unittest.TestCase):

    def test_lexer(self):
        #self.

    def test_parser(self):
        #self.

    def test_symbolTable(self):
        #self.

class LineBreakTestCase(unittest.TestCase):

    def test_lexer(self):
        #self.

    def test_parser(self):
        #self.

    def test_symbolTable(self):
        #self.

class MathTestCase(unittest.TestCase):

    def test_lexer(self):
        #self.

    def test_parser(self):
        #self.

    def test_symbolTable(self):
        #self.

class MultiLineCommentTestCase(unittest.TestCase):

    def test_lexer(self):
        #self.

    def test_parser(self):
        #self.

    def test_symbolTable(self):
        #self.

class PlainTestCase(unittest.TestCase):

    def test_lexer(self):
        #self.

    def test_parser(self):
        #self.

    def test_symbolTable(self):
        #self.

class SingleLineCommentTestCase(unittest.TestCase):

    def test_lexer(self):
        #self.

    def test_parser(self):
        #self.

    def test_symbolTable(self):
        #self.
"""
if __name__ == '__main__':
    unittest.main()
