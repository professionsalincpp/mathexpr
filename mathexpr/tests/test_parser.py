# test_parser.py

import unittest
from mathexpr import MathParse, ParserError

class TestParser(unittest.TestCase):
    def test_simple_expression(self):
        math_string = "2 + 3"
        result = MathParse.evaluate(math_string)
        self.assertEqual(result, 5)

    def test_complex_expression(self):
        math_string = "2 + 3 * 4 - 1"
        result = MathParse.evaluate(math_string)
        self.assertEqual(result, 13)

    def test_unary_expression(self):
        math_string = "-2 + 3"
        result = MathParse.evaluate(math_string)
        self.assertEqual(result, 1)

    def test_parenthesized_expression(self):
        math_string = "(2 + 3) * 4"
        result = MathParse.evaluate(math_string)
        self.assertEqual(result, 20)

    def test_invalid_expression(self):
        math_string = "2 +"
        
        with self.assertRaises(ParserError):
            MathParse.evaluate(math_string)

if __name__ == "__main__":
    unittest.main()