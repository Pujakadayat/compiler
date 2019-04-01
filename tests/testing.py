# pylint: disable=line-too-long

"""
Each test case has an accompanying class.
Each have methods such as: test_lexer, test_parser & test_symbolTable
"""

import unittest
from src.main import Compiler


class ArgumentsTestCase(unittest.TestCase):
    """Test case for arguments.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/arguments.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, sum, (, int, a, ,, int, b, ), {, return, a, +, b, ;, }, int, main, (, ), {, int, i, =, sum, (, 4, ,, 2, ), ;, i, =, sum, (, 2, ,, 4, ), ;, i, =, 2, ;, sum, (, 5, ,, i, ), ;, i, =, sum, (, 1, ,, 2, ), +, sum, (, 3, ,, 4, ), ;, return, i, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'sum': {'name': 'sum', '..': {...}, 'variables': {'a': 'int', 'b': 'int'}}, 'main': {'name': 'main', '..': {...}, 'variables': {'i': 'int'}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class AssignmentTestCase(unittest.TestCase):
    """Test case for assignment.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/assignment.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, int, x, =, 2, +, 2, ;, int, y, =, 5, ;, int, z, =, y, ;, x, =, y, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {'x': 'int', 'y': 'int', 'z': 'int'}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class AssignmentsTestCase(unittest.TestCase):
    """Test case for assignments.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/assignments.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, int, i, =, 0, ;, i, ++, ;, i, --, ;, i, +=, 2, ;, i, -=, 2, ;, return, i, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {'i': 'int'}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class BasicMathTestCase(unittest.TestCase):
    """Test case for basic_math.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/basic_math.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, return, 2, +, 2, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class CallTestCase(unittest.TestCase):
    """Test case for call.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/call.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, main, (, 2, ,, 3, ,, 5, ,, 6, ), ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class ControlFlowTestCase(unittest.TestCase):
    """Test case for control_flow.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/control_flow.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, int, i, =, 0, ;, int, y, =, 0, ;, int, x, =, 0, ;, for, (, i, =, 0, ;, i, <, 10, ;, i, ++, ), {, x, +=, 1, ;, }, while, (, i, >, 0, ), {, y, +=, 2, ;, i, --, ;, }, return, 0, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()


class DuplicateFuncTestCase(unittest.TestCase):
    """
    Test case for duplicate_func.c"
    Returns expected error, because of scope checking
    """

    @classmethod
    def setUpClass(cls):
        filename = "samples/duplicate_func.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, foo, (, ), {, return, 0, ;, }, int, foo, (, ), {, return, 1, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    @unittest.expectedFailure
    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()


class DuplicateVarTestCase(unittest.TestCase):
    """
    Test case for duplicate_var.c
    Returns expected error, because of scope checking
    """

    @classmethod
    def setUpClass(cls):
        filename = "samples/duplicate_var.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = (
            "[int, main, (, ), {, int, i, =, 0, ;, int, i, =, 1, ;, return, 0, ;, }, $]"
        )
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    @unittest.expectedFailure
    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()


class ExpressionTestCase(unittest.TestCase):
    """Test case for expression.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/expression.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, int, x, ;, x, =, 2, +, 2, ;, return, 0, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {'x': 'int'}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class FloatTestCase(unittest.TestCase):
    """Test case for float.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/float.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, float, x, =, 2.5, ;, return, x, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {'x': 'float'}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class ForTestCase(unittest.TestCase):
    """Test case for for.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/for.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, int, number, =, 10, ;, int, i, =, 0, ;, int, y, =, 0, ;, for, (, i, =, 0, ;, i, <, number, ;, i, ++, ), {, y, +=, 1, ;, }, return, 0, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {'number': 'int', 'i': 'int', 'y': 'int'}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class FunctionTestCase(unittest.TestCase):
    """Test case for function.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/function.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[stdio.h, int, sum, (, int, a, ,, int, b, ), {, return, a, +, b, ;, }, int, main, (, void, ), {, int, x, =, 2, ;, int, y, =, 5, ;, int, z, =, sum, (, x, ,, y, ), ;, printf, (, %d, ,, z, ), ;, return, 0, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    @unittest.expectedFailure
    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()


class HelloWorldTestCase(unittest.TestCase):
    """Test case for hello_world.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/hello_world.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[stdio.h, int, main, (, ), {, printf, (, Hello world!, ), ;, return, 0, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    @unittest.expectedFailure
    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()


class IfElseTestCase(unittest.TestCase):
    """Test case for if_else.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/if_else.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, int, number, =, 0, ;, if, (, number, ==, 0, ), {, number, =, 1, ;, }, else, {, number, =, 2, ;, }, return, 0, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {'number': 'int'}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class IfTestCase(unittest.TestCase):
    """Test case for if.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/if.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, int, number, =, 0, ;, if, (, number, ==, 0, ), {, number, =, 99, ;, }, return, 0, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {'number': 'int'}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class IncludeTestCase(unittest.TestCase):
    """Test case for include.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/include.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[stdio.h, int, main, (, ), {, return, 0, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class IRFuncTestCase(unittest.TestCase):
    """Test case for ir.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/ir.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, int, i, ;, int, j, ;, j, =, i, /, 12, *, 15, ;, return, i, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {'i': 'int', 'j': 'int'}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class LineBreakTestCase(unittest.TestCase):
    """Test case for linebreak.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/linebreak.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, char, string, =, Line 1 Line 2, ;, return, string, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {'string': 'char'}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class MathTestCase(unittest.TestCase):
    """Test case for math.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/math.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, int, i, =, 0, ;, i, +=, 25, ;, i, ++, ;, float, y, =, 2.5, ;, return, i, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table"""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {'i': 'int', 'y': 'float'}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class MultiLineCommentTestCase(unittest.TestCase):
    """Test case for multi_line_comment.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/multi_line_comment.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, return, 0, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table."""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class MultiFunctionsTestCase(unittest.TestCase):
    """Test case for multiple_functions.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/multiple_functions.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, foo, (, ), {, return, 0, ;, }, int, bar, (, ), {, return, 0, ;, }, int, foobar, (, ), {, return, 0, ;, }, int, foobiz, (, ), {, return, 0, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table."""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'foo': {'name': 'foo', '..': {...}, 'variables': {}}, 'bar': {'name': 'bar', '..': {...}, 'variables': {}}, 'foobar': {'name': 'foobar', '..': {...}, 'variables': {}}, 'foobiz': {'name': 'foobiz', '..': {...}, 'variables': {}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class MultiStatementsTestCase(unittest.TestCase):
    """Test case for multiple_statements.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/multiple_statements.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, int, x, ;, int, y, ;, int, z, ;, x, =, 2, ;, y, =, 2, ;, z, =, 2, ;, x, =, 2, +, 2, ;, }, int, foo, (, ), {, return, 0, ;, }, int, bar, (, ), {, return, 0, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table."""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {'x': 'int', 'y': 'int', 'z': 'int'}}, 'foo': {'name': 'foo', '..': {...}, 'variables': {}}, 'bar': {'name': 'bar', '..': {...}, 'variables': {}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class ParenthesesTestCase(unittest.TestCase):
    """Test case for parentheses.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/parentheses.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, int, i, ;, i, =, (, 2, ), ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table."""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {'i': 'int'}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class ParseTestCase(unittest.TestCase):
    """Test case for parseTest.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/parseTest.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, int, i, =, 10, ;, i, =, (, 4, +, 2, ), *, (, 10, %, 11, ), /, (, 3, +, (, 4, /, 2, ), ), ;, return, i, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table."""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {'i': 'int'}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class PlainTestCase(unittest.TestCase):
    """Test case for plain.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/plain.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, return, 1, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table."""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class SingleLineCommentTestCase(unittest.TestCase):
    """Test case for single_line_comment.c"""

    @classmethod
    def setUpClass(cls):
        filename = "samples/single_line_comment.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, return, 0, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    def test_symbolTable(self):
        """Test the result of the symbol table."""

        self.compiler.buildSymbolTable()
        result = "{'name': 'global', 'variables': [], 'main': {'name': 'main', '..': {...}, 'variables': {}}}"
        self.assertEqual(str(self.compiler.symbolTable), result)


class UndefinedVarTestCase(unittest.TestCase):
    """
    Test case for undefined_var.c
    Returns expected error, because of scope checking
    """

    @classmethod
    def setUpClass(cls):
        filename = "samples/undefined_var.c"
        cls.compiler = Compiler({"filename": filename})

    def test_lexer(self):
        """Test the result of the lexer."""

        self.compiler.tokenize()
        result = "[int, main, (, ), {, return, x, ;, }, $]"
        self.assertEqual(str(self.compiler.tokens), result)

    def test_parser(self):
        """Test if the tokens were parsed succesfully."""

        self.compiler.parse()
        self.assertTrue(self.compiler.parseTree)

    @unittest.expectedFailure
    def test_symbolTable(self):
        """Test the result of the symbol table."""

        self.compiler.buildSymbolTable()


if __name__ == "__main__":
    unittest.main()
