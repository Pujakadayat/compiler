"""
Integration tests for the compiler.
"""

import unittest
import src.main as main

class AssignmentTest(unittest.TestCase):
    def test_random(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_lex(self):
        filename = "samples/assignment.c"
        grammar = "grammars/main_grammar.txt"
        flags = ["-f", "-p"]

        isAcceptedByParser = main.run(filename, grammar, flags)
        self.assertEqual(isAcceptedByParser, True)

if __name__ == "__main__":
    unittest.main()
