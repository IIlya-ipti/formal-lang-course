from typing import Tuple
from pyformlang.cfg import Production, Variable, Terminal, CFG, Epsilon
import pyformlang
import networkx as nx
import queue as q
from collections import defaultdict
from .task2 import *
from .task6 import *
from scipy.sparse import dok_matrix
import copy


def mult_(left_: dict, right_: dict, rules_: dict):
    result = {}
    for varl in left_:
        for varr in right_:
            body = (varl, varr)
            if body in rules_:
                for head in rules_[body]:
                    if head in result:
                        result[head] += left_[varl] @ right_[varr]
                    else:
                        result[head] = left_[varl] @ right_[varr]

            body = (varr, varl)
            if body in rules_:
                for head in rules_[body]:
                    if head in result:
                        result[head] += right_[varr] @ left_[varl]
                    else:
                        result[head] = right_[varr] @ left_[varl]
    return result


def addition_(left_: dict, right_: dict, copy=True):
    result = {}
    for varl in left_:
        result[varl] = dok_matrix(left_[varl], copy=copy)

    for varr in right_:
        if varr in result:
            result[varr] = result[varr] + right_[varr]
        else:
            result[varr] = dok_matrix(right_[varr], copy=copy)
    return result


def cfpq_with_matrix(
    cfg: pyformlang.cfg.CFG,
    graph: nx.DiGraph,
    start_nodes: Set[int] = None,
    final_nodes: Set[int] = None,
) -> set[tuple[int, int]]:
    cfg: CFG = cfg_to_weak_normal_form(cfg)

    if start_nodes is None:
        start_nodes = graph.nodes

    if final_nodes is None:
        final_nodes = graph.nodes

    productions_by_body = defaultdict(lambda: set())
    productions_by_head = defaultdict(lambda: set())
    production_eps = {p for p in cfg.productions if len(p.body) == 0}

    for v in cfg.productions:
        if len(v.body) == 0:
            continue
        productions_by_body[tuple(v.body)].add(v.head)
        productions_by_head[v.head].add(tuple(v.body))

    def get_matrx(n: int, m: int):
        return dok_matrix((n, m), dtype=bool)

    # create matrix
    M = {}

    n = len(graph.nodes())

    for non_terminal in cfg.variables:
        M[non_terminal] = get_matrx(n, n)

    # init matrix (terminals to variable)
    _, _, edges = get_nvertex_nedges_numerate_marks_from_graph(graph)

    for edge in edges:
        vi, vj, label = edge
        term = Terminal(label)
        if tuple([term]) not in productions_by_body:
            continue
        for i in productions_by_body[tuple([term])]:
            M[i][vi, vj] = True

    # for epsilon
    for var in production_eps:
        for i in range(n):
            M[var.head][i, i] = True

    # algorithm
    N = len(cfg.variables)
    V = len(graph.nodes())

    total_iters = V * N
    for i in range(total_iters):
        M_tmp = mult_(M, M, productions_by_body)
        M = addition_(M, M_tmp)

    return {
        (i, j)
        for i in graph.nodes()
        for j in graph.nodes()
        if (i in start_nodes)
        and (j in final_nodes)
        and M[cfg.start_symbol][i, j] == True
    }
