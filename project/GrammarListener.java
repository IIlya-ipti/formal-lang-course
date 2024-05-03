// Generated from Grammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link GrammarParser}.
 */
public interface GrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link GrammarParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(GrammarParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(GrammarParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(GrammarParser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(GrammarParser.StmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#declare}.
	 * @param ctx the parse tree
	 */
	void enterDeclare(GrammarParser.DeclareContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#declare}.
	 * @param ctx the parse tree
	 */
	void exitDeclare(GrammarParser.DeclareContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#bind}.
	 * @param ctx the parse tree
	 */
	void enterBind(GrammarParser.BindContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#bind}.
	 * @param ctx the parse tree
	 */
	void exitBind(GrammarParser.BindContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#remove}.
	 * @param ctx the parse tree
	 */
	void enterRemove(GrammarParser.RemoveContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#remove}.
	 * @param ctx the parse tree
	 */
	void exitRemove(GrammarParser.RemoveContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#add}.
	 * @param ctx the parse tree
	 */
	void enterAdd(GrammarParser.AddContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#add}.
	 * @param ctx the parse tree
	 */
	void exitAdd(GrammarParser.AddContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(GrammarParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(GrammarParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#set_expr}.
	 * @param ctx the parse tree
	 */
	void enterSet_expr(GrammarParser.Set_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#set_expr}.
	 * @param ctx the parse tree
	 */
	void exitSet_expr(GrammarParser.Set_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#edge_expr}.
	 * @param ctx the parse tree
	 */
	void enterEdge_expr(GrammarParser.Edge_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#edge_expr}.
	 * @param ctx the parse tree
	 */
	void exitEdge_expr(GrammarParser.Edge_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#regexp}.
	 * @param ctx the parse tree
	 */
	void enterRegexp(GrammarParser.RegexpContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#regexp}.
	 * @param ctx the parse tree
	 */
	void exitRegexp(GrammarParser.RegexpContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#range}.
	 * @param ctx the parse tree
	 */
	void enterRange(GrammarParser.RangeContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#range}.
	 * @param ctx the parse tree
	 */
	void exitRange(GrammarParser.RangeContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#select}.
	 * @param ctx the parse tree
	 */
	void enterSelect(GrammarParser.SelectContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#select}.
	 * @param ctx the parse tree
	 */
	void exitSelect(GrammarParser.SelectContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#v_filter}.
	 * @param ctx the parse tree
	 */
	void enterV_filter(GrammarParser.V_filterContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#v_filter}.
	 * @param ctx the parse tree
	 */
	void exitV_filter(GrammarParser.V_filterContext ctx);
}
