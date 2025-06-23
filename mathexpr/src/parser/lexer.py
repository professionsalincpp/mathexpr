# Lexer to mathparse library
from enum import Enum
from .tokens import *
from ..utils.check import *
from ..utils.errors import ParserError

class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.current_char = text[self.position]
        self.tokens = TokensSequence()

    def input(self, text):
        self.text = text
        self.position = 0
        self.current_char = self.text[self.position]
        self.tokens = TokensSequence()

    def advance(self) -> str:
        self.position += 1
        self.current_char = self.text[self.position] if self.position < len(self.text) else None
        return self.current_char
    
    def skip_whitespace(self) -> str:
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
        return self.current_char
    
    def get_next_token(self) -> Token | None:
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                number = ''
                while check_is_number(self.current_char):
                    number += self.current_char
                    self.advance()
                return self.tokens.add(Token(TokenType.NUMBER, number))
            if self.current_char.isalpha():
                name = ''
                while check_is_identifier(self.current_char):
                    name += self.current_char
                    self.advance()
                return self.tokens.add(Token(TokenType.IDENTIFIER, name))
            if self.current_char == '(':
                val = self.tokens.add(Token(TokenType.LPAR, self.current_char))
                self.advance()
                return val
            if self.current_char == ')':
                val = self.tokens.add(Token(TokenType.RPAR, self.current_char))
                self.advance()
                return val
            if self.current_char == '+':
                val = self.tokens.add(Token(TokenType.ADD, self.current_char))
                self.advance()
                return val
            if self.current_char == '-':
                val = self.tokens.add(Token(TokenType.SUB, self.current_char))
                self.advance()
                return val
            if self.current_char == '*':
                val = self.tokens.add(Token(TokenType.MUL, self.current_char))
                self.advance()
                return val
            if self.current_char == '/':
                val = self.tokens.add(Token(TokenType.DIV, self.current_char))
                self.advance()
                return val
            if self.current_char == '=':
                val = self.tokens.add(Token(TokenType.ASSIGN, self.current_char))
                self.advance()
                return val
            if self.current_char == '^':
                val = self.tokens.add(Token(TokenType.POW, self.current_char))
                self.advance()
                return val
            
            raise ParserError(f"Unexpected character: {self.current_char}")
        
    def tokenize(self):
        while self.current_char is not None and not self.error:
            self.get_next_token()
        return self.tokens
    
    
    
