# Lexer to mathparse library
from .tokens import *
from ..utils.check import *
from ..utils.errors import ParserError, LexerError



class Lexer:
    def __init__(self, text="0.0"):
        """
        Initialize the Lexer with an input text
        """
        self.text = text
        self.position = 0
        self.current_char = text[self.position]
        self.tokens = TokensSequence()

    def input(self, text):
        """
        Set the input text and reset the position and current character
        """
        self.text = text
        self.position = 0
        self.current_char = self.text[self.position]
        self.tokens = TokensSequence()

    def advance(self) -> str:
        """
        Advance the position and set the current character
        """
        self.position += 1
        self.current_char = self.text[self.position] if self.position < len(self.text) else None
        return self.current_char
    
    def peek(self) -> str:
        """
        Peek at the next character without advancing the position
        """
        if self.position + 1 < len(self.text):
            return self.text[self.position + 1]
        else:
            return None
    
    def skip_whitespace(self) -> str:
        """
        Skip whitespace characters
        """
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
        return self.current_char
    
    def get_next_token(self) -> Token | None:
        """
        Get the next token from the input string
        """
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
            if self.current_char == '=' and self.peek() == '=':
                self.advance()
                val = self.tokens.add(Token(TokenType.EQ, '=='))
                self.advance()
                return val
            if self.current_char == '^':
                val = self.tokens.add(Token(TokenType.POW, self.current_char))
                self.advance()
                return val
            if self.current_char == '!':
                if self.peek() == '=':
                    self.advance()
                    val = self.tokens.add(Token(TokenType.NEQ, '!='))
                    self.advance()
                    return val
                raise ParserError("Invalid character: !")
            if self.current_char == '<':
                if self.peek() == '=':
                    self.advance()
                    val = self.tokens.add(Token(TokenType.LTE, '<'))
                    self.advance()
                    return val
                val = self.tokens.add(Token(TokenType.LT, self.current_char))
                self.advance()
                return val
            if self.current_char == '>':
                if self.peek() == '=':
                    self.advance()
                    val = self.tokens.add(Token(TokenType.GTE, '>'))
                    self.advance()
                    return val
                val = self.tokens.add(Token(TokenType.GT, self.current_char))
                self.advance()
                return val
            return self.handle_other_char() 
    
    def handle_other_char(self):
        """
        Use this function to handle other characters in subclasses
        """
        raise LexerError(f"Unexpected character: {self.current_char}")
        
    def tokenize(self):
        while self.current_char is not None:
            self.get_next_token()
        tok = self.tokens
        self.input(self.text)
        return tok
    
    

