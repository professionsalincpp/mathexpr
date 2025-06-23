# visitor.py
from ..utils.errors import *
from ..parser.tokens import TokenType
from typing import Dict

class NodeVisitor:
    """Abstract base class for node visitors"""
    def __init__(self, var_values: Dict[str, float] = {}) -> None:
        self.var_values = var_values
        self.vars = {}
        self.assignments = {}

    def visit(self, node) -> float | Exception:
        method_name = f"visit_{node.__class__.__name__}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node) -> Exception:
        raise Exception(f"No visit_{node.__class__.__name__} method")

    def visit_BinaryOpNode(self, node) -> float | Exception:
        left_value = self.visit(node.left)
        right_value = self.visit(node.right)
        if node.token.type == TokenType.ADD:
            return left_value + right_value
        elif node.token.type == TokenType.SUB:
            return left_value - right_value
        elif node.token.type == TokenType.MUL:
            return left_value * right_value
        elif node.token.type == TokenType.DIV:
            return left_value / right_value
        elif node.token.type == TokenType.POW:
            return left_value ** right_value
        else:
            raise UnknownBinaryOperatorError(f"Unknown binary operator {node.token.type}")

    def visit_UnaryOpNode(self, node) -> float | Exception:
        value = self.visit(node.expr)
        if node.token.type == TokenType.ADD:
            return +value
        elif node.token.type == TokenType.SUB:
            return -value
        else:
            raise UnknownUnaryOperatorError(f"Unknown unary operator {node.token.type}")

    def visit_NumNode(self, node) -> float:
        return node.token.value

    def visit_VarNode(self, node) -> float:
        if node.token.value in self.var_values:
            return self.var_values[node.token.value]
        raise UndefinedIdentifierError(f"Undefined identifier '{node.token.value}'")