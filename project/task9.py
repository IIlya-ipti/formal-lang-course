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
from .task7 import cfg_to_weak_normal_form
import scipy as sp
from .task8 import *
from pyformlang.finite_automaton import TransitionFunction, EpsilonNFA, Symbol, State, NondeterministicTransitionFunction
from copy import deepcopy


def add_tmp_automation(rsm: RecursiveAutomaton, label : str):
    nfa = ndfa.NondeterministicFiniteAutomaton()
    state0 = State(0)
    state1 = State(1)
    state2 = State(2)

    start_symbol = rsm.initial_label
    symbol = Symbol("alpha")

    nfa.add_start_state(state0)
    nfa.add_final_state(state2)
    nfa.add_transition(state0, start_symbol, state1)
    nfa.add_transition(state1, symbol, state2)
    rsm.add_box(Box(nfa, Symbol(label)))
    return rsm

def cfpq_with_gll1(
    cfg_or_rsm: CFG | RecursiveAutomaton,
    graph: nx.DiGraph,
    start_nodes: set[int] = None,
    final_nodes: set[int] = None,
) -> set[tuple[int, int]]:

    rsm = (
        cfg_or_rsm
        if isinstance(cfg_or_rsm, RecursiveAutomaton)
        else cfg_to_rsm(cfg_or_rsm)
    )

    start_nodes = graph.nodes if start_nodes is None else start_nodes
    final_nodes = graph.nodes if final_nodes is None else final_nodes

    rsm_start_nonterminal = rsm.initial_label.value

    stack_start_states = {
        (rsm_start_nonterminal, start_node) for start_node in start_nodes
    }
    stack_graph = {st: set() for st in stack_start_states}

    rsm_start_state = rsm.boxes[rsm.initial_label].dfa.start_state.value
    visited = {
        ((rsm_start_nonterminal, rsm_start_state), st[1], st)
        for st in stack_start_states
    }
    to_visit = deepcopy(visited)

    popped = {}
    res = set()

    while len(to_visit) != 0:
        rsm_state, graph_node, stack_state = to_visit.pop()

        if State(rsm_state[1]) in rsm.boxes[rsm_state[0]].dfa.final_states:
            if stack_state in stack_start_states:
                if graph_node in final_nodes:
                    res.add((stack_state[1], graph_node))

            popped.setdefault(stack_state, set()).add(graph_node)
            for to_stack_state, to_rsm_state in stack_graph.setdefault(
                stack_state, set()
            ):
                new_state = (to_rsm_state, graph_node, to_stack_state)
                if new_state not in visited:
                    to_visit.add(new_state)
                    visited.add(new_state)

        to_nodes = {}
        for _, n, l in graph.edges(graph_node, data="label"):
            to_nodes.setdefault(l, set()).add(n)

        dfa_dict = rsm.boxes[Symbol(rsm_state[0])].dfa.to_dict()
        if State(rsm_state[1]) not in dfa_dict:
            continue
        for symbol, to in dfa_dict[State(rsm_state[1])].items():
            if symbol in rsm.labels:
                new_stack_state = (symbol.value, graph_node)
                if new_stack_state in popped:
                    for to_graph_node in popped[new_stack_state]:
                        new_state = (
                            (rsm_state[0], to.value),
                            to_graph_node,
                            stack_state,
                        )
                        if new_state not in visited:
                            to_visit.add(new_state)
                            visited.add(new_state)
                stack_graph.setdefault(new_stack_state, set()).add(
                    (stack_state, (rsm_state[0], to.value))
                )
                start_state = rsm.boxes[symbol].dfa.start_state.value
                new_state = ((symbol.value, start_state), graph_node, new_stack_state)
                if new_state not in visited:
                    to_visit.add(new_state)
                    visited.add(new_state)
            else:
                if symbol.value not in to_nodes:
                    continue
                for node in to_nodes[symbol.value]:
                    new_state = ((rsm_state[0], to.value), node, stack_state)
                    if new_state not in visited:
                        to_visit.add(new_state)
                        visited.add(new_state)
    return res

def cfpq_with_gll(
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

    start_nodes = graph.nodes if start_nodes is None else start_nodes
    final_nodes = graph.nodes if final_nodes is None else final_nodes

    new_init_label = "S_____"
    rsm = add_tmp_automation(rsm,new_init_label)
    
    dict_rsm = { i : rsm.boxes[i].dfa.to_dict() for i in rsm.boxes}
    dict_rsm_start = { i : rsm.boxes[i].dfa.start_states for i in rsm.boxes}
    dict_rsm_final = { i : rsm.boxes[i].dfa.final_states for i in rsm.boxes}
    dict_rsm_states = { i : rsm.boxes[i].dfa.states for i in rsm.boxes}
    

    node_to_popped = defaultdict(lambda : set())
    node_to_state = {}
    state_to_node = {}
    gss = defaultdict(lambda : defaultdict(lambda : set()))

    def clear():
        node_to_popped.clear()
        node_to_state.clear()
        state_to_node.clear()
        gss.clear()

    inc = 0
    def create_node(symb, graph_state):
        if (symb, graph_state) in state_to_node:
            return state_to_node[(symb, graph_state)]
        nonlocal inc
        label = "g" + str(inc)
        inc += 1
        node_to_state[label] = (symb, graph_state)
        state_to_node[node_to_state[label]] = label
        return label

    def add_to_gss(from_, to_, label):
        gss[from_][to_].add(label)
    
    def handle_popped(g_from,g_to, pi):
        result = set()
        for i in node_to_popped[g_from]:
            _,v,_ = i
            result = result.union(set([(pi, v,g_to)]))
        return result


    def handle(d : tuple):
        (vi, node ,gk) = d

        symb_gk, _ = node_to_state[gk]

        nodes = graph.adj[node]

        dict_by_label_graph = defaultdict(lambda : set())
        for i in nodes:
            for labels in nodes[i]:
                dict_by_label_graph[nodes[i][labels]['label']].add(i)
        
        dict_by_label_rsm = defaultdict(lambda : set())
        # todo test by vi
        if vi in dict_rsm[symb_gk]:
            for i in dict_rsm[symb_gk][vi]:
                to = dict_rsm[symb_gk][vi][i]
                for labels in to if isinstance(to, set) else {to}:
                    dict_by_label_rsm[i].add(labels)
        
        new_desk = set()

        for symb in dict_by_label_rsm:
            #first
            if symb in dict_by_label_graph:
                for nodej in dict_by_label_graph[symb]:
                    for vj in dict_by_label_rsm[symb]:
                        new_desk.add((vj,nodej,gk))
            # second
            if symb in dict_rsm:
                new_g = create_node(symb, node)
                for pi in dict_by_label_rsm[symb]:
                    add_to_gss(new_g,gk,pi)
                    new_desk = new_desk.union(handle_popped(new_g, gk, pi))
                for qs in dict_rsm_start[symb]:
                    new_desk.add((qs, node, new_g))
                
            #third
            # if symb in dict_rsm_final:
        if vi in dict_rsm_final[symb_gk]:
            for g_old in gss[gk]:
                for pi in gss[gk][g_old]:
                    new_desk.add((pi,node,g_old))
                    node_to_popped[gk].add(d)

        return new_desk
            
    result = set()
    for start_node in start_nodes:
        clear()
        Dproc = set()
        for start_rsm_node in dict_rsm_start[new_init_label]:
            config = (start_rsm_node, start_node, create_node(new_init_label, start_node))
            Dproc.add(config)

        Dhandled = set()
        while len(Dproc) != 0:
            d = Dproc.pop()

            g_tmp = node_to_state[d[2]]


            if d[0] == '1' and g_tmp[0] == new_init_label and d[1] in final_nodes:
                result.add((start_node, d[1]))


            new_ds = handle(d)
            
            new_ds_tmp = set()
            # filter
            for i in new_ds:
                if i not in Dhandled:
                    new_ds_tmp.add(i)
            new_ds = new_ds_tmp
            Dhandled = Dhandled.union(set([d]))
            Dproc = Dproc.union(new_ds)
    return result