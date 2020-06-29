#---------------------------------------------------------------------------
# cateAnalysis_problem2.py
# This function calculates the two-tailed Fisher exact test.
#
# Designed by HsinYu (Katie) Chi
# 05 March 2019
#---------------------------------------------------------------------------

#- Imports
import numpy as np
from scipy.stats import hypergeom
from scipy.stats import fisher_exact

#- Function

def fisherexacttwotails(table):
    """
    Calculate the Fisher Exact Test with two sided, which is
    H0: p1 = p2 and Ha: p1 != p2

    Arguments:
        table {list} -- [description]
    """

    table_array = np.array(table)
    row0 = np.sum(table_array[0,:])
    row1 = np.sum(table_array[1,:])
    col0 = np.sum(table_array[:,0])
    col1 = np.sum(table_array[:,1])

    # calculate probabilities of all possible tables
    max_X = np.min([row0, col1])
    N = row0 + row1
    m = col0
    k = row0
    X = np.arrange(max_X + 1)
    possible_table_probab = hypergeom.pmf(X, N, m, k)
    observed_probab = hypergeom.pmf(table_array[0,0], N, m, k)

    more_extreme = possible_table_probab <= observed_probab
    return np.sum(possible_table_probab * more_extreme)

#===== end file =====