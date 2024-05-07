from .task3 import *
from .task2 import *
from scipy.sparse import hstack
from scipy.sparse import dok_matrix
from scipy.sparse import block_diag
from collections import defaultdict


def diagonalize_ones_matrix(matrix: dok_matrix, m: int) -> dok_matrix:
    if matrix is None:
        return matrix
    matrix = matrix.toarray()
    g = np.zeros(shape=matrix.shape, dtype=matrix.dtype)
    for i in range(matrix.shape[0] // m):
        for j in range(m):
            g[i * m + j] = matrix[i * m : i * m + m][
                matrix[i * m : i * m + m, j] > 0
            ].sum(axis=0)
    return dok_matrix(g)


def reachability_with_constraints(
    fa: FiniteAutomaton, constraints_fa: FiniteAutomaton
) -> dict[int, set[int]]:
    main = fa.get_matrix_word()
    constraints = constraints_fa.get_matrix_word()

    st_states_fa = fa.get_start_states()
    st_states_constraints_fa = constraints_fa.get_start_states()

    m = fa.get_n_states()
    n = constraints_fa.get_n_states()

    result = defaultdict(lambda: set())

    for sti in st_states_fa:
        for stj in st_states_constraints_fa:

            F = dok_matrix((m, m + n), dtype=np.bool_)

            F[0, sti] = True
            F[0, m + stj] = True

            F = diagonalize_ones_matrix(F, m)

            for _ in range(m * n):
                res = None
                for word in main:
                    if word not in constraints:
                        continue

                    M_work = block_diag((main[word], constraints[word]))
                    F_next = diagonalize_ones_matrix(F @ M_work, m)
                    if res is None:
                        res = F_next
                    else:
                        res += F_next
                if res is None:
                    break
                F = res

                for stifinal in fa.get_final_states():
                    if F[stifinal, stifinal] == 0:
                        continue

                    for stjfinal in constraints_fa.get_final_states():
                        if F[stifinal, m + stjfinal] > 0:
                            result[sti].add(stifinal)
    return result
