from antlr4 import *
from .GrammarLexer import GrammarLexer
from .GrammarParser import GrammarParser

from antlr4 import *
from antlr4.InputStream import InputStream


def prog_to_tree(program: str) -> tuple[ParserRuleContext, bool]:
    parser = GrammarParser(CommonTokenStream(GrammarLexer(InputStream(program))))
    prog = parser.prog()
    correct = parser.getNumberOfSyntaxErrors() == 0
    return (prog, correct)


def nodes_count(tree: ParserRuleContext) -> int:
    if not tree:
        return 0
    count = 1
    for i in range(tree.getChildCount()):
        count += nodes_count(tree.getChild(i))
    return count


def tree_to_prog(tree: ParserRuleContext) -> str:
    if not tree:
        return ""
    if tree.getChildCount() == 0:
        return tree.getText()
    res = ""
    for i in range(tree.getChildCount()):
        res += tree_to_prog(tree.getChild(i)) + " "
    return res
