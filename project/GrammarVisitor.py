# Generated from project/Grammar.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.


class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#prog.
    def visitProg(self, ctx: GrammarParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#stmt.
    def visitStmt(self, ctx: GrammarParser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#declare.
    def visitDeclare(self, ctx: GrammarParser.DeclareContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#bind.
    def visitBind(self, ctx: GrammarParser.BindContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#remove.
    def visitRemove(self, ctx: GrammarParser.RemoveContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#add.
    def visitAdd(self, ctx: GrammarParser.AddContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#expr.
    def visitExpr(self, ctx: GrammarParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#set_expr.
    def visitSet_expr(self, ctx: GrammarParser.Set_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#edge_expr.
    def visitEdge_expr(self, ctx: GrammarParser.Edge_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#regexp.
    def visitRegexp(self, ctx: GrammarParser.RegexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#range.
    def visitRange(self, ctx: GrammarParser.RangeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#select.
    def visitSelect(self, ctx: GrammarParser.SelectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#v_filter.
    def visitV_filter(self, ctx: GrammarParser.V_filterContext):
        return self.visitChildren(ctx)


del GrammarParser
