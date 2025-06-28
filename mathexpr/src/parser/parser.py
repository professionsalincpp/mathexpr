# parser.py
from .tokens import TokenType
from .lexer import Lexer
from ..ast.node import *
from ..utils.errors import ParserError

class Parser:
    """Parser for mathematical expressions"""

    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
        self._line = 0


    def error(self, message="Invalid syntax"):
        raise ParserError("Syntax error: " + message)

    def eat(self, token_type, error_msg: str = "Invalid syntax"):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(error_msg)

    def factor(self):
        token = self.current_token
        if token is None:
            return None
        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER, "Not a number")
            token.value = float(token.value)
            return NumNode(token)
        elif token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER, "Not an identifier")
            return VarNode(token)
        elif token.type == TokenType.SUB:
            self.eat(TokenType.SUB, "Not a '-'")
            node = UnaryOpNode(token, self.factor())
            return node
        elif token.type == TokenType.LPAR:
            self.eat(TokenType.LPAR, "Not a '('")
            node = self.expr()
            self.eat(TokenType.RPAR, "Expected ')'")
            return node
        else:
            self.error(f"Token type is '{token.type}'")

    def term(self):
        node = self.power()
        while self.current_token is not None and self.current_token.type in (TokenType.MUL, TokenType.DIV):
            token = self.current_token
            if token.type == TokenType.MUL:
                self.eat(TokenType.MUL)
            elif token.type == TokenType.DIV:
                self.eat(TokenType.DIV)
            factor = self.power()
            if factor is None:
                raise ParserError("Unexpected end of expression")
            node = BinaryOpNode(node, token, factor)
        return node

    def expr(self):
        node = self.term()
        while self.current_token is not None and self.current_token.type in (TokenType.ADD, TokenType.SUB):
            token = self.current_token
            if token.type == TokenType.ADD:
                self.eat(TokenType.ADD)
            elif token.type == TokenType.SUB:
                self.eat(TokenType.SUB)
            term = self.term()
            if term is None:
                raise ParserError("Unexpected end of expression")
            node = BinaryOpNode(node, token, term)
        return node
    
    def condition(self):
        node = self.factor()
        while self.current_token is not None and self.current_token.type in (TokenType.EQ, TokenType.NEQ, TokenType.LT, TokenType.LTE, TokenType.GT, TokenType.GTE):
            token = self.current_token
            if self.current_token.type == TokenType.EQ:
                self.eat(TokenType.EQ)
                right = self.expr()
                if right is None:
                    raise ParserError("Unexpected end of expression")
                node = BinaryOpNode(node, token, right)
            elif self.current_token.type == TokenType.NEQ:
                self.eat(TokenType.NEQ)
                right = self.expr()
                if right is None:
                    raise ParserError("Unexpected end of expression")
                node = BinaryOpNode(node, token, right)
            elif self.current_token.type == TokenType.LT:
                self.eat(TokenType.LT)
                right = self.expr()
                if right is None:
                    if right is None:
                        raise ParserError("Unexpected end of expression")
                node = BinaryOpNode(node, token, right)
            elif self.current_token.type == TokenType.LTE:
                self.eat(TokenType.LTE)
                right = self.expr()
                if right is None:
                    raise ParserError("Unexpected end of expression")
                node = BinaryOpNode(node, token, right)
            elif self.current_token.type == TokenType.GT:
                self.eat(TokenType.GT)
                right = self.expr()
                if right is None:
                    raise ParserError("Unexpected end of expression")
                node = BinaryOpNode(node, token, right)
            elif self.current_token.type == TokenType.GTE:
                self.eat(TokenType.GTE)
                right = self.expr()
                if right is None:
                    raise ParserError("Unexpected end of expression")
                node = BinaryOpNode(node, token, right)
        return node
    
    
    def power(self):
        node = self.condition()
        while self.current_token is not None and self.current_token.type in (TokenType.POW,):
            token = self.current_token
            self.eat(TokenType.POW)
            factor = self.factor()
            if factor is None:
                raise ParserError("Unexpected end of expression")
            node = BinaryOpNode(node, token, factor)
        return node

    def parse(self):
        node = self.expr()
        if self.current_token is not None:
            self.error("Unexpected token")
        return node