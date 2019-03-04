"""
Each test case has an accompanying class.
Each have methods such as: test_lexer, test_parser & test_symbolTable
"""

import unittest
from src.main import Compiler


class AssignmentTestCase(unittest.TestCase):
    """Test case for assignment.c"""

    def setUp(self):
        filename = "samples/assignment.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, int, x, =, 2, +, 2, ;, int, y, =, 5, ;, int, z, =, y, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#    def test_symbolTable(self):
#        filename = "samples/assignment.c"
#        grammar = "grammars/main_grammar.txt"
#        flags = ["-"]


class BasicMathTestCase(unittest.TestCase):
    """Test case for basic_math.c"""

    def setUp(self):
        filename = "samples/basic_math.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, return, 2, +, 2, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


class ExpressionTestCase(unittest.TestCase):
    """Test case for expression.c"""

    def setUp(self):
        filename = "samples/expression.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, int, x, ;, x, =, 2, ==, 2, ;, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


class FloatTestCase(unittest.TestCase):
    """Test case for float.c"""

    def setUp(self):
        filename = "samples/float.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, float, x, =, 2, ., 5, ;, return, x, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


class ForTestCase(unittest.TestCase):
    """Test case for for.c"""

    def setUp(self):
        filename = "samples/for.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, int, number, =, 10, ;, int, i, =, 0, ;, int, y, =, 0, ;, for, (, i, =, 0, ;, i, <, number, ;, i, ++, ), {, y, +=, 1, ;, }, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


class FunctionTestCase(unittest.TestCase):
    """Test case for function.c"""

    def setUp(self):
        filename = "samples/function.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[#, include, <, stdio, ., h, >, int, sum, (, int, a, int, b, ), {, return, a, +, b, ;, }, int, main, (, void, ), {, int, x, =, 2, ;, int, y, =, 5, ;, int, z, =, sum, (, x, y, ), ;, printf, (, ', %, d, \, n, ', z, ), ;, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


class HelloWorldTestCase(unittest.TestCase):
    """Test case for hello_world.c"""
    def setUp(self):
        filename = "samples/hello_world.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[<, stdio, ., h, >, int, main, (, void, ), {, printf, (, ', Hello, world, !, \n, ', ), ;, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


class IfElseTestCase(unittest.TestCase):
    """Test case for if_else.c"""

    def setUp(self):
        filename = "samples/if_else.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, int, number, =, 0, ;, if, (, number, ==, 0, ), {, number, =, 1, ;, }, else, {, number, =, 2, ;, }, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


class IfTestCase(unittest.TestCase):
    """Test case for if.c"""
    def setUp(self):
        filename = "samples/if.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, int, number, =, 0, ;, if, (, number, ==, 0, ), {, number, =, 99, ;, }, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


class IncludeTestCase(unittest.TestCase):
    """Test case for include.c"""

    def setUp(self):
        filename = "samples/include.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[#, include, <, stdio, ., h, >, int, main, (, ), {, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


class LineBreakTestCase(unittest.TestCase):
    """Test case for linebreak.c"""

    def setUp(self):
        filename = "samples/linebreak.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, char, *, string, =, ', Line 1, \, Line, 2, ', ;, return, string, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


class MathTestCase(unittest.TestCase):
    """Test case for math.c"""
    def setUp(self):
        filename = "samples/math.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, int, i, =, 0, ;, i, +=, 25, ;, i, ++, ;, float, y, =, 2, ., 5, ;, return, i, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


class MultiLineCommentTestCase(unittest.TestCase):
    """Test case for multi_line_comment.c"""

    def setUp(self):
        filename = "samples/multi_line_comment.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


class PlainTestCase(unittest.TestCase):
    """Test case for plain.c"""

    def setUp(self):
        filename = "samples/plain.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, return, 1, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


class SingleLineCommentTestCase(unittest.TestCase):
    """Test case for single_line_comment.c"""

    def setUp(self):
        filename = "samples/single_line_comment.c"
        self.compiler = Compiler(filename, grammar=None, flags=None)
        self.tokens = self.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        isAcceptedByParser = self.compiler.parse()
        self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


if __name__ == "__main__":
    unittest.main()
