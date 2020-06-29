#---------------------------------------------------------------------------
# cateAnalysis_problem3.py
# This function calculates the p-value given an input contingency table 
# using the chi-squared test of independence for an r row, c column 
# contingency table without using for or while loops.
#
# Designed by HsinYu (Katie) Chi
# 05 March 2019
#---------------------------------------------------------------------------

#- Imports
import numpy as np

#- Function
def chisquare(table):
    """
    This function calculates the p-value given an input contingency table 
    using the chi-squared test of independence for an r row, c column 
    contingency table without using for or while loops.

    Arguments:
        table {list} -- [description]
    """

    # I use the same idea of taking the table as an array, and calculate
    # the sum of each row and column, which Professor Johnny Lin shows
    # in the class.
    table_array = np.array(table)
    row0 = np.sum(table_array[0, :])  # 374 + 2629
    row1 = np.sum(table_array[1, :])  # 73 + 1219
    col0 = np.sum(table_array[:, 0])  # 374 + 73
    col1 = np.sum(table_array[:, 1])  # 2629 + 1219
    total = col0 + col1

    # Calculate the expected contingency
    newRow0 = (row0 * col0) / total
    newRow1 = (row0 * row1) / total
    newCol0 = (col0 * row0) / total
    newCol1 = (col0 * col1) / total

    # Calculate the chi squared t test
    chisquared = ((table_array[0] - newRow0)/newRow0) + \
        ((table_array[1] - newRow1)/newRow1) + \
            ((table_array[2] - newCol0)/newCol0) + \
                ((table_array[3] - newCol1)/newCol1)

    print(chisquared)

#===== end file =====
