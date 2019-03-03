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


# class ExpressionTestCase(unittest.TestCase):
#     def test_lexer(self):
#         filename = "samples/expression.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-s"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     def test_parser(self):
#         filename = "samples/expression.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-p"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


# class FloatTestCase(unittest.TestCase):
#     def test_lexer(self):
#         filename = "samples/float.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-s"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     def test_parser(self):
#         filename = "samples/float.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-p"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


# class ForTestCase(unittest.TestCase):
#     def test_lexer(self):
#         filename = "samples/for.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-s"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     def test_parser(self):
#         filename = "samples/for.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-p"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


# class FunctionTestCase(unittest.TestCase):
#     def test_lexer(self):
#         filename = "samples/function.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-s"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     def test_parser(self):
#         filename = "samples/function.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-p"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


# class HelloWorldTestCase(unittest.TestCase):
#     def test_lexer(self):
#         filename = "samples/hello_world.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-s"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     def test_parser(self):
#         filename = "samples/hello_world.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-p"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


# class IfElseTestCase(unittest.TestCase):
#     def test_lexer(self):
#         filename = "samples/if_else.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-s"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     def test_parser(self):
#         filename = "samples/if_else.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-p"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


# class IfTestCase(unittest.TestCase):
#     def test_lexer(self):
#         filename = "samples/if.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-s"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     def test_parser(self):
#         filename = "samples/if.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-p"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


# class IncludeTestCase(unittest.TestCase):
#     def test_lexer(self):
#         filename = "samples/include.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-s"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     def test_parser(self):
#         filename = "samples/include.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-p"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


# class LineBreakTestCase(unittest.TestCase):
#     def test_lexer(self):
#         filename = "samples/linebreak.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-s"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     def test_parser(self):
#         filename = "samples/linebreak.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-p"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


# class MathTestCase(unittest.TestCase):
#     def test_lexer(self):
#         filename = "samples/math.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-s"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     def test_parser(self):
#         filename = "samples/math.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-p"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


# class MultiLineCommentTestCase(unittest.TestCase):
#     def test_lexer(self):
#         filename = "samples/multi_line_comment.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-s"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     def test_parser(self):
#         filename = "samples/multi_line_comment.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-p"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


# class PlainTestCase(unittest.TestCase):
#     def test_lexer(self):
#         filename = "samples/plain.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-s"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     def test_parser(self):
#         filename = "samples/plain.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-p"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


# class SingleLineCommentTestCase(unittest.TestCase):
#     def test_lexer(self):
#         filename = "samples/single_line_comment.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-s"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     def test_parser(self):
#         filename = "samples/single_line_comment.c"
#         grammar = "grammars/main_grammar.txt"
#         flags = ["-p"]

#         isAcceptedByParser = main.run(filename, grammar, flags)
#         self.assertEqual(isAcceptedByParser, True)

#     # def test_symbolTable(self):
#     # self.


if __name__ == "__main__":
    unittest.main()
