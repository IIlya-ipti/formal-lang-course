from typing import Iterable, List, Set
from networkx import MultiDiGraph
import pyformlang.regular_expression as re
import pyformlang.finite_automaton.deterministic_finite_automaton as dfa
import pyformlang.finite_automaton.nondeterministic_finite_automaton as ndfa
from pyformlang.finite_automaton import State
import scipy as sp
from scipy.sparse import dok_matrix
import numpy as np
import queue
from itertools import tee
from typing import Union
import project.task2 as tsk2
from itertools import product
from pyformlang.finite_automaton import Symbol
from scipy.sparse import *


class FiniteAutomaton:

    @staticmethod
    def get_matrix(n: int, m: int):
        return dok_matrix((n, m), dtype=np.bool_)

    @staticmethod
    def df_to_matrix(
        map_to_id: dict, df: dfa.DeterministicFiniteAutomaton
    ) -> dok_matrix:
        dict_df = df.to_dict()

        matrix_word = dict()

        n = len(df.states)

        for from_ in dict_df:

            from_id = map_to_id[from_]
            by_from = dict_df[from_]

            for label in by_from:

                if label not in matrix_word:
                    matrix_word[label] = FiniteAutomaton.get_matrix(n, n)

                to = by_from[label]
                for id in to if isinstance(to, set) else {to}:
                    to_id = map_to_id[id]
                    matrix_word[label][from_id, to_id] = 1
        return matrix_word

    def __init__(
        self,
        df: Union[
            dfa.DeterministicFiniteAutomaton, ndfa.NondeterministicFiniteAutomaton
        ] = None,
        start_states: Set = None,
        final_states: Set = None,
        states: Set = None,
        matrix: dok_matrix = None,
        map_to_id: dict = None,
        map_from_id: dict = None,
        epsilon_states: set = None,
    ):
        if start_states is None:
            start_states = set()

        if final_states is None:
            final_states = set()

        if matrix is not None:
            self.start_states = start_states
            self.final_states = final_states
            self.states = states
            self.map_to_id = map_to_id
            self.map_from_id = map_from_id
            self.matrix_word = matrix
            self.epsilon_states = epsilon_states
            return

        self.start_states: Set[int] = start_states
        self.final_states: Set[int] = final_states
        self.states = list()

        self.map_to_id: dict = {}
        self.map_from_id: dict = {}

        for id, state in enumerate(df.states):
            self.map_to_id[state] = id
            self.map_from_id[id] = state
            self.states.append(id)

        self.start_states = self.start_states.union(
            (self.map_to_id[i.value] for i in df.start_states)
        )
        self.final_states = self.final_states.union(
            (self.map_to_id[i.value] for i in df.final_states)
        )

        self.matrix_word = FiniteAutomaton.df_to_matrix(self.map_to_id, df=df)

    def _add(left_dict: dict, right_dict: dict):
        dict_result = {}
        for i in left_dict:
            dict_result[i] = dok_matrix(left_dict[i], copy=True)

        for i in right_dict:
            if i in dict_result:
                dict_result[i] += right_dict[i]
            else:
                dict_result[i] = dok_matrix(right_dict[i], copy=True)
        return dict_result

    def accepts(self, word: Iterable[Symbol]) -> bool:
        q = queue.Queue()

        for i in self.start_states:
            it = iter(word)
            q.put((i, it))

        while not q.empty():
            head, it = q.get()

            # has next
            it, new_it = tee(it)

            try:
                next_symb = next(it)
            except StopIteration:
                return head in self.final_states

            if not (next_symb in self.matrix_word):
                continue
            for i in range(self.matrix_word[next_symb].shape[1]):
                if self.matrix_word[next_symb][head, i] == True:
                    it, new_it = tee(it)
                    q.put((i, new_it))
        return False

    def get_n_states(self) -> int:
        return len(self.states)

    def get_start_states(self):
        return self.start_states

    def get_final_states(self):
        return self.final_states

    def is_empty(self) -> bool:
        transitive_close = self.get_transitive_close()
        for i in self.start_states:
            for j in self.final_states:
                if transitive_close[i, j] > 0:
                    return False
        return True

    def get_transitive_close(self):
        n = len(self.states)
        bool_matrix = FiniteAutomaton.get_matrix(n, n)
        bool_matrix += eye(n, dtype=bool)
        for i in self.matrix_word:
            bool_matrix |= self.matrix_word[i]

        for _ in range(n):
            bool_matrix += bool_matrix @ bool_matrix
        return bool_matrix

    def get_matrix_word(self):
        return self.matrix_word


def intersect_automata(
    automaton1: FiniteAutomaton, automaton2: FiniteAutomaton
) -> FiniteAutomaton:

    map_first = automaton1.get_matrix_word()
    map_second = automaton2.get_matrix_word()
    map_result = dict()

    for i in map_first:
        if i not in map_second:
            continue
        else:
            left = map_first[i]
            right = map_second[i]
            cron = sp.sparse.kron(left, right, format="dok")
            map_result[i] = cron

    start = set()
    final = set()

    for sti in automaton1.start_states:
        for stj in automaton2.start_states:
            sti_new = len(automaton2.states) * sti + stj
            start.add(sti_new)

    for sti in automaton1.final_states:
        for stj in automaton2.final_states:
            sti_new = len(automaton2.states) * sti + stj
            final.add(sti_new)

    states = [i for i in range(0, len(automaton1.states) * len(automaton2.states))]
    return FiniteAutomaton(
        matrix=map_result, states=states, start_states=start, final_states=final
    )


def paths_ends(
    graph: MultiDiGraph, start_nodes: set[int], final_nodes: set[int], regex: str
) -> list[tuple]:
    graph_auto = FiniteAutomaton(tsk2.graph_to_nfa(graph, start_nodes, final_nodes))
    regex_auto = FiniteAutomaton(tsk2.regex_to_dfa(regex))

    ins = intersect_automata(graph_auto, regex_auto)

    transitive_close = ins.get_transitive_close()
    result = set()

    for st in ins.start_states & ins.final_states:
        n = st // len(regex_auto.states)
        result.add((n, n))

    for i in ins.start_states:
        for j in ins.final_states:
            if transitive_close[i, j] > 0:
                m = len(regex_auto.states)
                result.add(((i // m), (j // m)))
    return list(result)
