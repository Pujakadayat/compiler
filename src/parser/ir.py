"""
Methods and classes related to
Intermediate Representations of the Parse Tree.
"""

from src.parser.grammar import FunctionDeclaration


def generateIr(parseTree):
    """Generate an intermediate representation from a parse tree."""

    ir = []
    visitChildren(parseTree, ir)
    return ir


def visitChildren(node, ir):
    """Visit each node of the parse tree."""

    if isinstance(node, FunctionDeclaration):
        ir.append(node.ir())

    if hasattr(node, "children"):
        for child in node.children:
            visitChildren(child, ir)
    elif isinstance(node, list):
        for child in node:
            visitChildren(child, ir)

    if not isinstance(node, list):
        if not isinstance(node, FunctionDeclaration):
            i = node.ir()
            if i is not None and not i.isdigit():
                ir.append(i)
