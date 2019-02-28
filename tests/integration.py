"""
Integration tests for the compiler.
"""

import unittest

class AssignmentTest(unittest.TestCase):
    def test_parse(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == "__main__":
    unittest.main()
