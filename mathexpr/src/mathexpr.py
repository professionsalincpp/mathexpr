# mathparse.py

import mathexpr
from typing import List, Dict
from .utils.debug import print_ast
from .parser.lexer import Lexer
from .parser.parser import Parser, ParserError
from .ast.node import Node, BinaryOpNode, UnaryOpNode, NumNode, VarNode
from .ast.visitor import NodeVisitor, UndefinedIdentifierError
from .utils.debug import * 


class MathExpr:
    """Math parsing class"""

    @staticmethod
    def parse(math_string: str) -> Node:
        """Parse a mathematical string into an AST"""
        lexer = Lexer(math_string)
        parser = Parser(lexer)
        ast = parser.parse()
        return ast
    
    @staticmethod
    def evaluateast(ast: Node, variables: Dict[str, float] = {}) -> float:
        """Evaluate an AST"""
        return NodeVisitor(variables).visit(ast)

    @classmethod
    def evaluate(cls, math_string: str, variables: Dict[str, float] = {}) -> float:
        """Evaluate a mathematical string"""
        ast: Node = cls.parse(math_string)
        result: float = cls.evaluateast(ast, variables)
        return result