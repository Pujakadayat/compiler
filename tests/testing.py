# pylint: disable=line-too-long

"""
Each test case has an accompanying class.
Each have methods such as: test_lexer, test_parser & test_symbolTable
"""

import unittest
from src.main import Compiler


class AssignmentTestCase(unittest.TestCase):
    """Test case for assignment.c"""

    @classmethod
    def setUpClass(cls,):
        filename = "samples/assignment.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, int, x, =, 2, +, 2, ;, int, y, =, 5, ;, int, z, =, y, ;, x, =, y, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#    def test_symbolTable(self):
#        filename = "samples/assignment.c"
#        grammar = "grammars/main_grammar.txt"
#        flags = ["-"]


class BasicMathTestCase(unittest.TestCase):
    """Test case for basic_math.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/basic_math.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, return, 2, +, 2, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#     # def test_symbolTable(self):
#     # self.


class ExpressionTestCase(unittest.TestCase):
    """Test case for expression.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/expression.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, int, x, ;, x, =, 2, +, 2, ;, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#     # def test_symbolTable(self):
#     # self.


class FloatTestCase(unittest.TestCase):
    """Test case for float.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/float.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, float, x, =, 2.5, ;, return, x, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#     # def test_symbolTable(self):
#     # self.


class ForTestCase(unittest.TestCase):
    """Test case for for.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/for.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, int, number, =, 10, ;, int, i, =, 0, ;, int, y, =, 0, ;, for, (, i, =, 0, ;, i, <, number, ;, i, ++, ), {, y, +=, 1, ;, }, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#     # def test_symbolTable(self):
#     # self.


class FunctionTestCase(unittest.TestCase):
    """Test case for function.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/function.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[stdio.h, int, sum, (, int, a, ,, int, b, ), {, return, a, +, b, ;, }, int, main, (, void, ), {, int, x, =, 2, ;, int, y, =, 5, ;, int, z, =, sum, (, x, ,, y, ), ;, printf, (, %d, ,, z, ), ;, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#     # def test_symbolTable(self):
#     # self.


class HelloWorldTestCase(unittest.TestCase):
    """Test case for hello_world.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/hello_world.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[stdio.h, int, main, (, ), {, printf, (, Hello world!, ), ;, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#     # def test_symbolTable(self):
#     # self.


class IfElseTestCase(unittest.TestCase):
    """Test case for if_else.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/if_else.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, int, number, =, 0, ;, if, (, number, ==, 0, ), {, number, =, 1, ;, }, else, {, number, =, 2, ;, }, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#     # def test_symbolTable(self):
#     # self.


class IfTestCase(unittest.TestCase):
    """Test case for if.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/if.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, int, number, =, 0, ;, if, (, number, ==, 0, ), {, number, =, 99, ;, }, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#     # def test_symbolTable(self):
#     # self.


class IncludeTestCase(unittest.TestCase):
    """Test case for include.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/include.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[stdio.h, int, main, (, ), {, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#     # def test_symbolTable(self):
#     # self.


class LineBreakTestCase(unittest.TestCase):
    """Test case for linebreak.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/linebreak.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, char, string, =, Line 1 Line 2, ;, return, string, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#     # def test_symbolTable(self):
#     # self.


class MathTestCase(unittest.TestCase):
    """Test case for math.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/math.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, int, i, =, 0, ;, i, +=, 25, ;, i, ++, ;, float, y, =, 2.5, ;, return, i, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#     # def test_symbolTable(self):
#     # self.


class MultiLineCommentTestCase(unittest.TestCase):
    """Test case for multi_line_comment.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/multi_line_comment.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#     # def test_symbolTable(self):
#     # self.


class PlainTestCase(unittest.TestCase):
    """Test case for plain.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/plain.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, return, 1, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#     # def test_symbolTable(self):
#     # self.


class SingleLineCommentTestCase(unittest.TestCase):
    """Test case for single_line_comment.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/single_line_comment.c"
        cls.compiler = Compiler(filename, grammar=None, flags=None)
        cls.tokens = cls.compiler.tokenize()

    def test_lexer(self):
        """Test the result of the lexer."""

        result = "[int, main, (, ), {, return, 0, ;, }, $]"
        self.assertEqual(str(self.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        parseTree = self.compiler.parse()
        self.assertTrue(parseTree)


#     # def test_symbolTable(self):
#     # self.


if __name__ == "__main__":
    unittest.main()
