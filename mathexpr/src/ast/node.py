# Node implementation for AST 


class Node:
    """Abstract base class for AST nodes"""

    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f"{self.__class__.__name__}(token={self.token})"


class BinaryOpNode(Node):
    """Node for binary operations (e.g., 2 + 3)"""

    def __init__(self, left, op, right):
        super().__init__(op)
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.__class__.__name__}(left={self.left}, op={self.token}, right={self.right})"


class UnaryOpNode(Node):
    """Node for unary operations (e.g., -2)"""

    def __init__(self, op, expr):
        super().__init__(op)
        self.expr = expr

    def __repr__(self):
        return f"{self.__class__.__name__}(op={self.token}, expr={self.expr})"


class NumNode(Node):
    """Node for numeric literals (e.g., 42)"""

    def __init__(self, token):
        super().__init__(token)

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.token.value})"


class VarNode(Node):
    """Node for variable references (e.g., x)"""

    def __init__(self, token):
        super().__init__(token)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.token.value})"