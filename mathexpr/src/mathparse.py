# mathparse.py

from typing import Dict
from .parser.lexer import Lexer
from .parser.parser import Parser, ParserError
from .ast.node import Node, BinaryOpNode, UnaryOpNode, NumNode, VarNode
from .ast.visitor import NodeVisitor


class MathParse:
    """Math parsing class"""

    @staticmethod
    def parse( math_string: str) -> Node:
        """Parse a mathematical string into an AST"""
        lexer = Lexer(math_string)
        parser = Parser(lexer)
        ast = parser.parse()
        return ast

    def evaluate(math_string: str, variables: Dict[str, float] = {}) -> float | Exception:
        """Evaluate a mathematical string"""
        ast = MathParse.parse(math_string)
        result = NodeVisitor().visit(ast)
        return result
