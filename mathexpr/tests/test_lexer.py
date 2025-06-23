# test_lexer.py

import unittest
from mathexpr.src.parser.lexer import Lexer
from mathexpr.src.parser.tokens import TokenType 

class TestLexer(unittest.TestCase):
    def test_number_token(self):
        lexer = Lexer("123")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.NUMBER)
        self.assertEqual(token.value, "123")

    def test_add_token(self):
        lexer = Lexer("+")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.ADD)

    def test_sub_token(self):
        lexer = Lexer("-")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.SUB)

    def test_mul_token(self):
        lexer = Lexer("*")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.MUL)

    def test_div_token(self):
        lexer = Lexer("/")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.DIV)

    def test_lparen_token(self):
        lexer = Lexer("(")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.LPAR)

    def test_rparen_token(self):
        lexer = Lexer(")")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.RPAR)

    def test_identifier_token(self):
        lexer = Lexer("x")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.IDENTIFIER)
        self.assertEqual(token.value, "x")

    def test_difficult_sequence(self):
        lexer = Lexer("1+2*(3-4)/5")
        tokens = []
        for _ in range(11):  # Test 10 times
            tokens.append(lexer.get_next_token())
        expected_tokens = [
            TokenType.NUMBER, TokenType.ADD, TokenType.NUMBER,
            TokenType.MUL, TokenType.LPAR, TokenType.NUMBER, TokenType.SUB, TokenType.NUMBER, TokenType.RPAR,
            TokenType.DIV, TokenType.NUMBER
        ]
        self.assertEqual([token.type for token in tokens], expected_tokens)


if __name__ == "__main__":
    unittest.main()