from GrammarVisitor import GrammarVisitor
from task11 import *
from pyformlang.regular_expression import Regex
import networkx as nx
from pyformlang.rsa import RecursiveAutomaton
from task8 import *


class TypeError(Exception):
    pass


# def copy(strin, n):
#     res = ""
#     for i in range(n):
#         res += strin
#     return res


# def to_new_val(inp):
#     val = inp.split("^")
#     print(val)
#     real_val = val[0]
#     tmp = val[1]
#     print(tmp)
#     first, second = tmp[1:-1].split("..")
#     return "|".join([copy(real_val, i) for i in range(int(first), int(second) + 1)])


# print(to_new_val("abc^[2..5]"))

# def mat_to_nfa(automaton: FiniteAutomaton) -> NondeterministicFiniteAutomaton:
#     nfa = NondeterministicFiniteAutomaton()

#     for label in automaton.m.keys():
#         m_size = automaton.m[label].shape[0]
#         for u in range(m_size):
#             for v in range(m_size):
#                 if automaton.m[label][u, v]:
#                     nfa.add_transition(
#                         automaton.mapping_for(u), label, automaton.mapping_for(v)
#                     )

#     for s in automaton.start:
#         nfa.add_start_state(automaton.mapping_for(s))
#     for s in automaton.final:
#         nfa.add_final_state(automaton.mapping_for(s))

#     return nfa


class TypeChecker(GrammarVisitor):
    Regex.to_cfg
    FA_type = "FA"
    RSM_type = "RSM"

    def __init__(self):
        self.types = {}
        self.vars = set()

    def visitDeclare(self, ctx: GrammarParser.DeclareContext):
        var = ctx.VAR().getText()
        self.vars.add(var)
        self.types[var] = "graph"
        return self.types[var]

    def visitBind(self, ctx: GrammarParser.BindContext):
        var = ctx.VAR().getText()
        self.vars.add(var)
        self.types[var] = self.visit(ctx.expr())
        return self.types[var]

    def visitExpr(self, ctx: GrammarParser.ExprContext):
        if ctx.CHAR():
            return "char"
        if ctx.NUM():
            return "int"
        if ctx.VAR():
            value = ctx.VAR().getText()
            if value not in self.types:
                self.RSM_type
            return self.types[value]
        if ctx.set_expr():
            return self.visit(ctx.set_expr())
        if ctx.edge_expr():
            return self.visit(ctx.edge_expr())
        if ctx.regexp():
            return self.visit(ctx.regexp())
        if ctx.select():
            return self.visit(ctx.select())
        raise TypeError("doesn't exists rule")

    def interspect_type(self, type1, type2):
        if type1 == self.FA_type and type2 == self.FA_type:
            return self.FA_type

        if type1 == self.RSM_type and type2 == self.FA_type:
            return self.RSM_type

        if type1 == self.FA_type and type2 == self.RSM_type:
            return self.RSM_type

        if type1 == self.RSM_type and type2 == self.RSM_type:
            raise TypeError("interspect rsm and rsm")

    def concat_type(self, type1, type2):
        if type1 == self.FA_type and type2 == self.FA_type:
            return self.FA_type

        if type1 == self.FA_type and type2 == self.RSM_type:
            return self.RSM_type

        if type1 == self.RSM_type and type2 == self.FA_type:
            return self.RSM_type

        if type1 == self.RSM_type and type2 == self.RSM_type:
            return self.RSM_type

    def union_type(self, type1, type2):
        if type1 == self.FA_type and type2 == self.FA_type:
            return self.FA_type

        if type1 == self.FA_type and type2 == self.RSM_type:
            return self.RSM_type

        if type1 == self.RSM_type and type2 == self.FA_type:
            return self.RSM_type

        if type1 == self.RSM_type and type2 == self.RSM_type:
            return self.RSM_type

    def visitRegexp(self, ctx: GrammarParser.RegexpContext):
        if ctx.getChildCount() == 1:
            if ctx.CHAR():
                return self.FA_type
            if ctx.VAR():
                if ctx.VAR().getText() in self.types:
                    tp = self.types[ctx.VAR().getText()]
                    if tp == self.RSM_type:
                        return tp
                    return self.FA_type
                return self.RSM_type
            raise TypeError("error type")
        elif ctx.getChildCount() == 3:
            a = ctx.getChild(0)
            operator = ctx.getChild(1).getText()
            b = ctx.getChild(2)
            if operator == ".":
                return self.concat_type(self.visit(a), self.visit(b))
            if operator == "|":
                return self.union_type(self.visit(a), self.visit(b))
            if operator == "&":
                a_type = self.visit(a)
                return self.interspect_type(a_type, self.visit(b))
            if operator == "^":
                tmp = self.visit(a)

                return tmp
            if str(ctx.getChild(0)) == "(" and str(ctx.getChild(2)) == ")":
                return self.visit(ctx.getChild(1))
            raise TypeError("error type")
        else:
            print("etf")

    def visitSelect(self, ctx: GrammarParser.SelectContext):

        Maybe = lambda x: None if x is None else self.visit(x)

        # type check filters
        Maybe(ctx.v_filter(0))
        Maybe(ctx.v_filter(1))

        left = -1
        for i in range(ctx.getChildCount()):
            if str(ctx.getChild(i)) == "return":
                left = i
                break
        reachable_ind = -1
        for i in range(ctx.getChildCount()):
            if str(ctx.getChild(i)) == "where":
                reachable_ind = i
                break
        returns = [
            ctx.getChild(i)
            for i in range(left + 1, reachable_ind)
            if str(ctx.getChild(i)) != ","
        ]
        q_type = self.visit(ctx.expr())
        if q_type == self.FA_type or q_type == self.RSM_type or q_type == "char":
            return "Set<" + " * ".join(["int" for i in returns]) + ">"
        raise TypeError(f"error type in visit select{q_type}")

    def visitV_filter(self, ctx: GrammarParser.V_filterContext):
        expr_type = self.visit(ctx.expr())
        if expr_type == "edge" or expr_type == "Set<int * int>":
            raise TypeError("error type in visit filter")
        return "filter"

    def visitRemove(self, ctx: GrammarParser.RemoveContext):
        type_of_remove_value = ctx.getChild(1)
        if type_of_remove_value.getText() == "edge":
            if self.visit(ctx.expr()) != "edge":
                raise TypeError("error type in visit remove")
        if type_of_remove_value.getText() == "vertex":
            if self.visit(ctx.expr()) != "int":
                raise TypeError("error type in visit remove")
        if type_of_remove_value.getText() == "vertices":
            tp = self.visit(ctx.expr())
            if tp != "Set<?>" and tp != "Set<int>":
                raise TypeError(f"error type in visit remove {tp}")
            print(self.visit(ctx.expr()))
        return "remove"

    def visitRange(self, ctx: GrammarParser.RangeContext):
        return "range"

    def visitSet_expr(self, ctx: GrammarParser.Set_exprContext):
        for i in range(ctx.getChildCount()):
            val = ctx.expr(i)
            if val is None:
                continue
            val_type = self.visit(val)
            if val_type != "int" and val_type != "edge":
                raise TypeError(f"error type in visit visitSet_expr {val_type}")
        return "Set<?>"

    def visitEdge_expr(self, ctx: GrammarParser.Edge_exprContext):
        all_types = [
            self.visit(ctx.expr(i))
            for i in range(ctx.getChildCount())
            if ctx.expr(i) != None
        ]
        if all_types[0] == "int" and all_types[1] == "char" and all_types[2] == "int":
            return "edge"
        raise TypeError("error type in visitEdge_expr")


def typing_program(program: str) -> bool:
    tree, correct = prog_to_tree(program)
    if not correct:
        print("Syntax error in program")
        return False
    type_checker = TypeChecker()
    try:
        type_checker.visit(tree)
        print(type_checker.types)
        return True
    except TypeError as e:
        print(f"Type error: {e}")
        return False


cnt = 0


def rsm_to_ebnf(rsm: RecursiveAutomaton):
    global cnt
    ebnf = ""
    for _, box in rsm.boxes.items():
        ebnf += box.label.value + " -> " + str(box.dfa._get_regex_simple()) + "\n"
    cnt += 1
    new_label = "S" + str(cnt)
    ebnf = ebnf.replace(rsm.initial_label.value, new_label)
    return (ebnf, new_label)


class Interpreter(GrammarVisitor):
    def __init__(self):
        self.globals = {}
        self.stack = []

    # # Visit a parse tree produced by GrammarParser#prog.
    # def visitProg(self, ctx:GrammarParser.ProgContext):
    #     return self.visitChildren(ctx)

    # # Visit a parse tree produced by GrammarParser#stmt.
    # def visitStmt(self, ctx:GrammarParser.StmtContext):
    #     return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#declare.
    def visitDeclare(self, ctx: GrammarParser.DeclareContext):
        var = ctx.VAR().getText()
        self.globals[var] = nx.MultiGraph()
        return None

    # Visit a parse tree produced by GrammarParser#bind.
    def visitBind(self, ctx: GrammarParser.BindContext):
        var = ctx.VAR().getText()
        self.globals[var] = self.visit(ctx.expr())
        return None

    # Visit a parse tree produced by GrammarParser#remove.
    def visitRemove(self, ctx: GrammarParser.RemoveContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#add.
    def visitAdd(self, ctx: GrammarParser.AddContext):
        var = ctx.VAR().getText()
        tp_of_add = ctx.getChild(1).getText()
        expr = ctx.expr().getText()
        if var not in self.globals:
            raise ValueError(f"Graph {var} is not declared")
        graph = self.globals[var]
        if tp_of_add == "vertex":
            vertex = int(ctx.expr().getText())
            graph.add_vertex(vertex)
        elif tp_of_add == "edge":
            (u, coeff, v) = self.visit(ctx.expr())
            graph.add_edge(u, v, key=coeff)
        return None

    # Visit a parse tree produced by GrammarParser#expr.
    def visitExpr(self, ctx: GrammarParser.ExprContext):
        if ctx.NUM():
            return int(ctx.NUM().getText())
        if ctx.CHAR():
            return ctx.CHAR().getText()
        if ctx.VAR():
            name = ctx.VAR().getText()
            if name not in self.globals:
                RuntimeError("Unknown expression")
            return self.globals[name]
        if ctx.set_expr():
            return self.visit(ctx.set_expr())
        if ctx.regexp():
            return self.visit(ctx.regexp())
        if ctx.edge_expr():
            return self.visit(ctx.edge_expr())
        raise RuntimeError("Unknown expression")

    # Visit a parse tree produced by GrammarParser#set_expr.
    def visitSet_expr(self, ctx: GrammarParser.Set_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#edge_expr.
    def visitEdge_expr(self, ctx: GrammarParser.Edge_exprContext):
        return (
            int(ctx.expr(0).getText()),
            ctx.expr(1).getText(),
            int(ctx.expr(2).getText()),
        )

    def rsm_concatenate(self, a: Regex, b: Regex) -> Regex:
        return a.concatenate(b)

    def rsm_union(self, a: Regex, b: Regex) -> Regex:
        return a.union(b)

    # def rsm_intersect(self, a : Regex, b : Regex) -> Regex:
    #     afg : CFG = a.to_cfg()
    #     afg.intersection(b)
    #     afg.to_pda
    #     rsm = rsm_to_matrix(rsm)
    #     intersection = intersect_automata(rsm, FiniteAutomaton(regex.to_epsilon_nfa()))

    #     return RecursiveAutomaton.from_regex(graph_to_nfa(intersection).to_regex()),

    # Visit a parse tree produced by GrammarParser#regexp.
    def visitRegexp(self, ctx: GrammarParser.RegexpContext):
        if ctx.getChildCount() == 1:
            if ctx.CHAR():
                return Regex(ctx.CHAR().getText())
            if ctx.VAR():
                if ctx.VAR().getText() in self.globals:
                    tp = self.types[ctx.VAR().getText()]
                    return tp
                return Regex("")
            raise TypeError("error type")
        elif ctx.getChildCount() == 3:
            a = ctx.getChild(0)
            operator = ctx.getChild(1).getText()
            b = ctx.getChild(2)
            if operator == ".":
                return self.rsm_concatenate(self.visit(a), self.visit(b))
            if operator == "|":
                return self.rsm_union(self.visit(a), self.visit(b))
            if operator == "&":
                a_type = self.visit(a)
                return self.rsm_intersect(a_type, self.visit(b))
            if operator == "^":
                tmp = self.visit(a)
                return Regex(to_new_val(str(tmp)[1:-1] + "^" + b.getText()))
            if str(ctx.getChild(0)) == "(" and str(ctx.getChild(2)) == ")":
                return self.visit(ctx.getChild(1))
            raise TypeError("error type")
        else:
            print("etf")

    def visitRange(self, ctx: GrammarParser.RangeContext):
        return self.visitChildren(ctx)

    def visitSelect(self, ctx: GrammarParser.SelectContext):
        return self.visitChildren(ctx)

    def visitV_filter(self, ctx: GrammarParser.V_filterContext):
        return self.visitChildren(ctx)


def typing_program(program: str) -> bool:
    tree, correct = prog_to_tree(program)
    if not correct:
        print("Syntax error in program")
        return False
    type_checker = TypeChecker()
    try:
        type_checker.visit(tree)
        print(type_checker.types)
        return True
    except TypeError as e:
        print(f"Type error: {e}")
        return False


def exec_program(program: str) -> dict[str, set[tuple]]:
    tree, correct = prog_to_tree(program)
    if not correct:
        print("Syntax error in program")
        return False
    type_checker = Interpreter()
    try:
        type_checker.visit(tree)
        print(type_checker.globals)
        return type_checker.globals
    except TypeError as e:
        print(f"Type error: {e}")
        return False


# def test_typing_program():

#     program = """
#     let g is graph

#     add edge (1, "a", 2) to g
#     add edge (2, "a", 3) to g
#     add edge (3, "a", 1) to g
#     add edge (1, "c", 5) to g
#     add edge (5, "b", 4) to g
#     add edge (4, "b", 5) to g

#     let q = "a"^[1..3] . q . "b"^[2..3] | "c"


#     """
#     exec_program(program)


# test_typing_program()
