#------------------------------------------------------------------------------
# Wilcoxon rank-sum method.
#
# nonparametric2
# nonPara2_problem1.py
# 
# Designed by HsinYu (katie) Chi
#
# NOTE:It might has some errors.
# NOTE:The data sets I use are fake data.
#------------------------------------------------------------------------------

#- Imports

from collections import ChainMap
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#- Function

def wilcoxon(x, y):

    # Create the data.
    data = np.concatenate((x, y))
    data.sort()
    n = np.size(data)

    ranking = []
    for i in range(n):
        # NOTE: This part comes from the code made by Professor Johnny Lin
        # To generate the ranking, and if there is repeated numbers, ranking
        #  will be the sum of it.
        is_dupes = np.isclose(data[i], data)
        ranking[i] = np.sum(is_dupes * ranking) \
            / float(np.sum(is_dupes))

    wOfx = np.sum(np.where(data == x, ranking, 0.0))
    wOfy = np.sum(np.where(data == y, ranking, 0.0))
    W = np.minimum(wOfx, wOfy)

    n1 = np.size(x)
    n2 = np.size(y)

    muOfW = n1 * (n1 + n2 + 1) / 2.0
    Sw = np.sqrt(n1 * n2 * (n1 + n2 + 1) / 12.0)

    Z = (W - muOfW) / Sw
    p_value = norm.cdf(Z)

    # Print the results
    print('Rankings: ' + ranking)
    print('W_x: ' + wOfx)
    print('W_y: ' + wOfy)
    print('W: ' + W)
    print('mu_W: ' + muOfW)
    print('S_W: ' + Sw)
    print('Z: ' + Z)
    print('p_value: ' + p_value)

    return W, p_value


if __name__ == "__main__":

    a = np.array([1.2, 2.0, 3.88, 6.16, 5.16, 7.77])
    b = np.array([3.3, 4.5, 6.5, 6.6, 5.8, 7.9])

    print("The result of fake data:")

#===== end file =====
