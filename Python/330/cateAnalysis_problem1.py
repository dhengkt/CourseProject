#---------------------------------------------------------------------------
# cateAnalysis_problem1.py
# This function will calculate the Hypergeometric Distribution by using the
# algorithm from Pishro-Nik's 3.1.5.
#
#
# Designed by HsinYu (Katie) Chi
# 05 March 2019
#---------------------------------------------------------------------------

#- Imports
import numpy as np
from itertools import combinations
from scipy.stats import hypergeom

#- Function
def hyperRedesigned(n, m, x, k):

    """[summary]
    Calculate the Hypergeometric Distribution by using the algorithm from
    Pishro-Nik's Book. (cannot use choose function)

    equation is ((n choose x) * (r choose k-x)) / (n+m choose k)
    
    Arguments:
        n {int} -- First group of sample
        m {int} -- Second group of sample
        x {int} -- Number of sample you want to choose
        k {int} -- Total number of ways to choose from n + m values
    """

    # calculate the n choose x first
    comb1 = combinations(n, x)
    comb2 = combinations(r, (k-x))
    comb3 = combinations((n+m), k)

    # take the len of the combinations lists and calculate the result
    a = len(comb1)
    b = len(comb2)
    c = len(comb3)

    return (a * b) / c


#===== end file =====
