#------------------------------------------------------------------------------
#
# ICA:nonparametric2
# ICAnonpara2.py
#
# HsinYu (katie) Chi
#
# NOTE:I only do the persuedocode here because it might take too much time to
# finish it.
#------------------------------------------------------------------------------

#- Import
import numpy as np
import collections

#- Function
def ICAnonpara_2():

    # Data
    asian = [9.84, 9.40, 8.20, 8.24, 9.20, 8.55, 8.52, 8.12]
    caucasian = [8.27, 8.20, 8.25, 8.14, 9.00, 8.10, 7.20, 8.30, 7.70]

    # Sort two groups of data in order
    allData = asian + caucasian
    allData.sort()

    ranking = []
    n = len(allData)
    for i in range(n):
        ranking[i] = i

    # Create a Map to store two set of data with the ranking
    rank_data = collections.ChainMap(allData, ranking)
    # Calculate the average ranking of data if there has same data
    

#===== End file =====