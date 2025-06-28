# Tokens to mathparse library
from enum import Enum
from typing import List


class OperationType(Enum):
    """
    Operations tokens
    """
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    DIV = "DIV"
    EXP = "EXP"
    MOD = "MOD"
    POW = "POW"
    ASSIGN = "ASSIGN"
    EQ = "EQU",
    NEQ = "NEQ",
    GT = "GT",
    LT = "LT",
    GTE = "GTE",
    LTE = "LTE"


class SyntaxType(Enum):
    """
    Syntax tokens
    """
    LPAR = "LPAR"
    RPAR = "RPAR"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    DOT = "DOT"
    COMMA = "COMMA"

class Keywords(Enum):
    IF = "IF",
    ELSE = "ELSE"

class TokenType(Enum):
    """
    All types of tokens
    """
    # Operations
    ADD = OperationType.ADD
    SUB = OperationType.SUB
    MUL = OperationType.MUL
    DIV = OperationType.DIV
    EXP = OperationType.EXP
    MOD = OperationType.MOD
    POW = OperationType.POW
    ASSIGN = OperationType.ASSIGN
    EQ = OperationType.EQ
    NEQ = OperationType.NEQ
    GT = OperationType.GT
    LT = OperationType.LT
    GTE = OperationType.GTE
    LTE = OperationType.LTE
    # Syntax
    LPAR = SyntaxType.LPAR
    RPAR = SyntaxType.RPAR
    LBRACE = SyntaxType.LBRACE
    RBRACE = SyntaxType.RBRACE 
    DOT = SyntaxType.DOT
    COMMA = SyntaxType.COMMA
    # Identifiers
    NUMBER = 'NUMBER'
    IDENTIFIER = 'IDENTIFIER'
    # Keywords
    EOF = 'EOF'
    IF = Keywords.IF,
    ELSE = Keywords.ELSE

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
    
    def __repr__(self):
        return f"Token: {self.type} {self.value}\n"
    

class TokensSequence:
    def __init__(self):
        self.tokens: List[Token] = []
        self.index = 0

    def add(self, token):
        self.tokens.append(token)
        return token
    
    def get(self, index=None):
        if index == None:
            return self.tokens[self.index]
        else:
            return self.tokens[index]
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.tokens):
            token = self.tokens[self.index]
            self.index += 1
            return token
        else:
            raise StopIteration
        
        return self

    def __len__(self):
        return len(self.tokens)
    
    def __str__(self):
        return str(self.tokens)
    
    def __repr__(self):
        return str(self.tokens)
        
    def __getitem__(self, index):
        return self.tokens[index]
        
    def __setitem__(self, index, value):
        self.tokens[index] = value
        return self
        
    def __delitem__(self, index):
        del self.tokens[index]
        return self
    
    def __contains__(self, value):
        return value in self.tokens
    
    def __eq__(self, other):
        return self.tokens == other.tokens
