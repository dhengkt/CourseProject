#------------------------------------------------------------------------------
#
# nonPara_problem4.py
# nonparametric analysis homework problem four.
#
# This program will read two files provided by Professor Johnny Lin, and
# calculate the C.I for them by using directly from the bootstrap distribution"
# method of using bootstrapping.
#
# Create by HsinYu (Katie) Chi on 16 Feb. 2019
#
#------------------------------------------------------------------------------

#- Import
import numpy as np
from scipy.stats import t
from scipy.stats import signal
from sklearn.utils import resample

#- Function
def problem4():

    # data from file "fat.dat.txt"
    # NOTE: Not sure what to put in other parameter to find exact values.
    less40 = np.genfromtxt("fat.dat.txt") #sample is younger than 40
    grea40 = np.genfromtxt("fat.dat.txt") #sample is older than 40

    # calculate the mean and standard deviation
    xBarles40 = np.mean(less40)
    xBargre40 = np.mean(grea40)

    # Replacing the samples.
    # NOTE: Not sure if resample method can use like this.
    newless40 = signal.resample(less40, 1000)
    newgrea40 = signal.resample(grea40, 1000)

    # After replacing the samples, calculate the t statstic of the bootstrap
    # samples.
    t_statistic_less40 = t.ppf(alpha / 2, np.size(newless40))
    t_statistic_grea40 = t.ppf(alpha / 2, np.size(newgrea40))

    # Find the new standard deviation
    stdles40 = np.std(newless40, N-1)
    stdgre40 = np.std(newgrea40, N-1)

    # calculate the C.I
    CI_less40_upper = xBarles40 + (t_statistic_less40 * stdles40)
    CI_less40_lower = xBarles40 - (t_statistic_less40 * stdles40)

    CI_grea40_upper = xBargre40 + (t_statistic_grea40 * stdgre40)
    CI_grea40_lower = xBargre40 - (t_statistic_grea40 * stdgre40)

    # print the results out
    print("(C.I for people younger than 40 ys old: ", CI_less40_lower, ", "
        , CI_less40_upper, ")")
    print("(C.I for people older than 40 ys old: ", CI_grea40_lower, ", "
        , CI_grea40_upper, ")")

#===== end file =====
