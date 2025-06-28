from ..ast.node import *
try:
    from mathlang import *
except ImportError:
    _Type = type("MathLangObject", (object,), {})
    AssignmentNode = _Type
    LineNode = _Type
    BlockNode = _Type

def print_ast(node, children=None, level=0, is_last=True):
    """
    Prints a tree representation of a node and its children.
    """
    prefix = ''
    if level > 0:
        for i in range(level - 1):
            prefix += '│  '
        if is_last:
            prefix += '╰──'
        else:
            prefix += '├──'
        
    node_name = ""
    if isinstance(node, BinaryOpNode) or isinstance(node, UnaryOpNode):
        node_name = str(node.token.type) 
    elif isinstance(node, AssignmentNode):
        node_name = "TokenType.ASSIGN"
    elif isinstance(node, LineNode):
        if node.line is not None:
            node_name = str(node.line)
        else:
            node_name = "None"
    elif isinstance(node, BlockNode):
        children = node.statements
        node_name = "BlockNode"
    else:
        if node is not None:
            node_name = str(node)
        else:
            node_name = "None"
    print(prefix + node_name)
    if isinstance(node, BinaryOpNode) or isinstance(node, AssignmentNode):
        children = [node.left, node.right]
    elif isinstance(node, UnaryOpNode):
        children = [node.expr]
    if isinstance(node, LineNode):
        children = [node.statement]
    elif isinstance(node, BlockNode):
        children = node.statements
    if children is not None:
        for i, child in enumerate(children):
            is_last_child = i == len(children) - 1
            print_ast(child, None, level + 1, is_last_child)


def print_token(token):
    if token is not None:
        print(f"Token: {token.type}, Value: {token.value}")
    else:
        print("Token: None")