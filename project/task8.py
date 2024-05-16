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
from pyformlang.rsa import RecursiveAutomaton
from pyformlang.rsa.box import Box
import pyformlang.regular_expression as re
from pyformlang.finite_automaton import Symbol
from .task3 import *
from collections import defaultdict
from .task7 import cfg_to_weak_normal_form, addition_
import scipy as sp
from pyformlang.finite_automaton import TransitionFunction, EpsilonNFA, Symbol, State


def rsm_to_matrix(rsm: RecursiveAutomaton) -> tuple:

    rsm_states = {
        (var.value, state)
        for (var, box) in rsm.boxes.items()
        for state in box.dfa.states
    }

    map_to_id = {s: id for (id, s) in enumerate(rsm_states)}
    map_from_id = {s: id for (id, s) in map_to_id.items()}

    rsm_start = {
        map_to_id[(var.value, start)]
        for (var, box) in rsm.boxes.items()
        for start in box.dfa.start_states
    }
    rsm_end = {
        map_to_id[(var.value, final)]
        for (var, box) in rsm.boxes.items()
        for final in box.dfa.final_states
    }

    n = len(rsm_states)

    matrix = defaultdict(lambda: FiniteAutomaton.get_matrix(n, n))
    for symb, box in rsm.boxes.items():
        for from_, trams in box.dfa.to_dict().items():
            for label, to_ in trams.items():
                from_idx = map_to_id[(symb.value, from_)]
                to_idx = map_to_id[(symb.value, to_)]
                matrix[label.value][from_idx, to_idx] = True

    return FiniteAutomaton(
        matrix=matrix,
        start_states=rsm_start,
        final_states=rsm_end,
        states=set([i for i in range(len(rsm_states))]),
        map_to_id=map_to_id,
        map_from_id=map_from_id,
    )


def cfpq_with_tensor(
    cfg_or_rsm: RecursiveAutomaton,
    graph: nx.DiGraph,
    start_nodes: set[int] = None,
    final_nodes: set[int] = None,
) -> set[tuple[int, int]]:

    rsm = (
        cfg_or_rsm
        if isinstance(cfg_or_rsm, RecursiveAutomaton)
        else cfg_to_rsm(cfg_or_rsm)
    )

    if start_nodes is None:
        start_nodes = graph.nodes

    if final_nodes is None:
        final_nodes = graph.nodes

    rsm_fa = rsm_to_matrix(rsm)
    graph_fa = FiniteAutomaton(
        graph_to_nfa(graph=graph, start_states=start_nodes, final_states=final_nodes)
    )

    r = rsm_fa.get_n_states()
    n = graph_fa.get_n_states()

    graph_tmp = graph_fa

    last = None

    new = 1

    ins_tmp = None

    while new > 0:
        new = 0
        ins = intersect_automata(graph_tmp, rsm_fa)

        if ins_tmp is not None:
            ins_ = addition_(ins.matrix_word, ins_tmp.matrix_word, copy=False)
            ins = FiniteAutomaton(matrix=ins_, states=ins.states)
            ins_tmp = ins
        else:
            ins_tmp = ins

        C = ins.get_transitive_close()

        points = list(zip(*C.nonzero()))

        tmp = {}

        for vi, vj in points:
            from_rsm, to_rsm = vi % r, vj % r

            if (from_rsm in rsm_fa.start_states) and (to_rsm in rsm_fa.final_states):
                symb_1 = rsm_fa.map_from_id[from_rsm]
                symb_2 = rsm_fa.map_from_id[to_rsm]

                if symb_1[0] != symb_2[0]:
                    raise RuntimeError()
                symb = symb_1[0]

                from_graph, to_graph = vi // r, vj // r

                if symb not in graph_fa.matrix_word:
                    graph_fa.matrix_word[symb] = FiniteAutomaton.get_matrix(n, n)

                #
                if graph_fa.matrix_word[symb][from_graph, to_graph] == False:
                    if symb not in tmp:
                        tmp[symb] = FiniteAutomaton.get_matrix(n, n)
                    tmp[symb][from_graph, to_graph] = True
                    new += 1

                graph_fa.matrix_word[symb][from_graph, to_graph] = True

        graph_tmp = FiniteAutomaton(
            matrix=tmp,
            start_states=graph_fa.start_states,
            final_states=graph_fa.final_states,
            states=graph_fa.states,
        )

    S = rsm.initial_label.value
    if S not in graph_fa.matrix_word:
        return set()

    result = {
        (i, j)
        for i in range(n)
        for j in range(n)
        if (i in start_nodes)
        and (j in final_nodes)
        and (graph_fa.matrix_word[S][i, j] == True)
    }
    return result


def cfg_to_rsm(cfg: CFG) -> RecursiveAutomaton:

    trunsactions = defaultdict(lambda: list())
    for trans in cfg.productions:
        if len(trans.body) == 0:
            trunsactions[trans.head].append("$")
        else:
            trunsactions[trans.head].append(" ".join(i.value for i in trans.body))

    boxs = set()
    labels = set()

    for head, body in trunsactions.items():
        st = "|".join(body)
        boxs.add(Box(regex_to_dfa(st), head))
        labels.add(head)
    start_symbol = cfg.start_symbol

    return RecursiveAutomaton(labels, start_symbol, boxs)


def ebnf_to_rsm(ebnf: str) -> RecursiveAutomaton:
    return RecursiveAutomaton.from_text(ebnf)
