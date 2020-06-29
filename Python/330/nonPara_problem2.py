#------------------------------------------------------------------------------
#
# nonPara_problem2.py
# nonparametric analysis homework problem two.
#
# Create by HsinYu (Katie) Chi on 16 Feb. 2019
# NOTE: I do not know how to do some part of the problem, so this program is not
# complete.
#
#------------------------------------------------------------------------------

#- Import:
import numpy as np
from scipy.stats import*

#- Function:
def problem2():

    # data from file "fat.dat.txt"
    # NOTE: Not sure what to put in other parameter to find exact values.
    lessthan40 = np.genfromtxt("fat.dat.txt") #sample is younger than 40
    greaterthan40 = np.genfromtxt("fat.dat.txt") #sample is older than 40

    # calculate the mean of two sets of data
    xBarles40 = np.mean(lessthan40)
    xBargre40 = np.mean(greaterthan40)

    # find the differences between those two data
    differen = xBarles40 - xBargre40

    # number of total differences
    differen_list = lessthan40 - greaterthan40
    numDiff = np.size(differen_list)

    # NOTE: I think it's doing the same thing like problem 1, but I do not know
    # how to do it exactly. So, I cannot finish this problem.

    # find whether those two data are the same

    # Print out the result
    print()

    #- Solution from Professor
    #raw_data = np.genfromtxt()
    #age = []


#===== end file =====
