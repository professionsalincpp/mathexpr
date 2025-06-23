from ..ast.node import *

def print_node(node, children=None, level=0, is_last=True):
    """
    Prints a tree representation of a node and its children.
    """
    prefix = ''
    if level > 0:
        for i in range(level - 1):
            prefix += '│   '
        if is_last:
            prefix += '╰──'
        else:
            prefix += '├──'
        
    node_name = ""
    if isinstance(node, BinaryOpNode) or isinstance(node, UnaryOpNode):
        node_name = str(node.token.type) 
    else:
        node_name = str(node.token.value)
    print(prefix + node_name)
    if isinstance(node, BinaryOpNode):
        children = [node.left, node.right]
    elif isinstance(node, UnaryOpNode):
        children = [node.expr]
    if children is not None:
        for i, child in enumerate(children):
            is_last_child = i == len(children) - 1
            print_node(child, None, level + 1, is_last_child)