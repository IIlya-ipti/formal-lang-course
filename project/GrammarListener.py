# Generated from project/Grammar.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser


# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#prog.
    def enterProg(self, ctx: GrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by GrammarParser#prog.
    def exitProg(self, ctx: GrammarParser.ProgContext):
        pass

    # Enter a parse tree produced by GrammarParser#stmt.
    def enterStmt(self, ctx: GrammarParser.StmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#stmt.
    def exitStmt(self, ctx: GrammarParser.StmtContext):
        pass

    # Enter a parse tree produced by GrammarParser#declare.
    def enterDeclare(self, ctx: GrammarParser.DeclareContext):
        pass

    # Exit a parse tree produced by GrammarParser#declare.
    def exitDeclare(self, ctx: GrammarParser.DeclareContext):
        pass

    # Enter a parse tree produced by GrammarParser#bind.
    def enterBind(self, ctx: GrammarParser.BindContext):
        pass

    # Exit a parse tree produced by GrammarParser#bind.
    def exitBind(self, ctx: GrammarParser.BindContext):
        pass

    # Enter a parse tree produced by GrammarParser#remove.
    def enterRemove(self, ctx: GrammarParser.RemoveContext):
        pass

    # Exit a parse tree produced by GrammarParser#remove.
    def exitRemove(self, ctx: GrammarParser.RemoveContext):
        pass

    # Enter a parse tree produced by GrammarParser#add.
    def enterAdd(self, ctx: GrammarParser.AddContext):
        pass

    # Exit a parse tree produced by GrammarParser#add.
    def exitAdd(self, ctx: GrammarParser.AddContext):
        pass

    # Enter a parse tree produced by GrammarParser#expr.
    def enterExpr(self, ctx: GrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#expr.
    def exitExpr(self, ctx: GrammarParser.ExprContext):
        pass

    # Enter a parse tree produced by GrammarParser#set_expr.
    def enterSet_expr(self, ctx: GrammarParser.Set_exprContext):
        pass

    # Exit a parse tree produced by GrammarParser#set_expr.
    def exitSet_expr(self, ctx: GrammarParser.Set_exprContext):
        pass

    # Enter a parse tree produced by GrammarParser#edge_expr.
    def enterEdge_expr(self, ctx: GrammarParser.Edge_exprContext):
        pass

    # Exit a parse tree produced by GrammarParser#edge_expr.
    def exitEdge_expr(self, ctx: GrammarParser.Edge_exprContext):
        pass

    # Enter a parse tree produced by GrammarParser#regexp.
    def enterRegexp(self, ctx: GrammarParser.RegexpContext):
        pass

    # Exit a parse tree produced by GrammarParser#regexp.
    def exitRegexp(self, ctx: GrammarParser.RegexpContext):
        pass

    # Enter a parse tree produced by GrammarParser#range.
    def enterRange(self, ctx: GrammarParser.RangeContext):
        pass

    # Exit a parse tree produced by GrammarParser#range.
    def exitRange(self, ctx: GrammarParser.RangeContext):
        pass

    # Enter a parse tree produced by GrammarParser#select.
    def enterSelect(self, ctx: GrammarParser.SelectContext):
        pass

    # Exit a parse tree produced by GrammarParser#select.
    def exitSelect(self, ctx: GrammarParser.SelectContext):
        pass

    # Enter a parse tree produced by GrammarParser#v_filter.
    def enterV_filter(self, ctx: GrammarParser.V_filterContext):
        pass

    # Exit a parse tree produced by GrammarParser#v_filter.
    def exitV_filter(self, ctx: GrammarParser.V_filterContext):
        pass


del GrammarParser
