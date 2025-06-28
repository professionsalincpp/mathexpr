# test_parser.py

import unittest
from mathexpr import MathExpr, ParserError, UndefinedIdentifierError, LexerError

class TestParser(unittest.TestCase):
    def test_simple_expression(self):
        math_string = "2 + 3"
        result = MathExpr.evaluate(math_string)
        self.assertEqual(result, 5)

    def test_complex_expression(self):
        math_string = "2 + 3 * 4 - 1"
        result = MathExpr.evaluate(math_string)
        self.assertEqual(result, 13)

    def test_unary_expression(self):
        math_string = "-2 + 3"
        result = MathExpr.evaluate(math_string)
        self.assertEqual(result, 1)

    def test_parenthesized_expression(self):
        math_string = "(2 + 3) * 4"
        result = MathExpr.evaluate(math_string)
        self.assertEqual(result, 20)

    def test_invalid_expression(self):
        math_string = "2 +"
        
        with self.assertRaises(ParserError):
            MathExpr.evaluate(math_string)

        math_string = "2 + 3 *"
        
        with self.assertRaises(ParserError):
            MathExpr.parse(math_string)

        math_string = "2 + 3 * 4 <"
        
        with self.assertRaises(ParserError):
            MathExpr.parse(math_string)

    def test_invalid_operator(self):
        math_string = "2 + * 3"
        
        with self.assertRaises(ParserError):
            MathExpr.parse(math_string)

    def test_variables(self):
        variables = {"x": 2, "y": 3}
        math_string = "x + y"
        result = MathExpr.evaluate(math_string, variables)
        self.assertEqual(result, 5)

    def test_invalid_variable(self):
        variables = {"x": 2, "y": 3}
        math_string = "x + z"
        
        with self.assertRaises(UndefinedIdentifierError):
            MathExpr.evaluate(math_string, variables)

        math_string = "z + y"
        
        with self.assertRaises(UndefinedIdentifierError):
            MathExpr.evaluate(math_string, variables)

    def test_condition_expression(self):
        math_string = "x < y"
        variables = {"x": 2, "y": 3}
        result = MathExpr.evaluate(math_string, variables)
        self.assertEqual(result, 1)

        math_string = "x > y"
        variables = {"x": 2, "y": 3}
        result = MathExpr.evaluate(math_string, variables)
        self.assertEqual(result, 0)

    def test_undefined_variable(self):
        math_string = "x + y"
        
        with self.assertRaises(UndefinedIdentifierError):
            MathExpr.evaluate(math_string)

if __name__ == "__main__":
    unittest.main()