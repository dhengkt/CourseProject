#-------------------------------------------------------------------------------
# ICA: problem 2
# ICA_CateAnaly_problem2.py
#
# Designed by HsinYu Chi
#
#
#--------------------------------------------------------------------------------

import numpy as np
from scipy.stats import hypergeom
from scipy.stats import fisher_exact


def fisherexact_greater(table):
    """
    Calculate the Fisher Exact Test with greater hypothesis, which is
    Ha: P1 > P2

    Arguments:
        table {[type]} -- [description]
    """

    table_array = np.array(table)

    possible_tables_probab = []
    max_X = np.min([total_row0, total_col1])
    N = total_row0 + total_row1
    m = total_col0
    k = total_row0

    for X in range(max_X + 1):
        if X >= table_array[0, 0]:
            probab = hypergeom.pmf(X, N, m, k)
            possible_tables_probab.append(probab)


    return np.sum(possible_tables_probab)
