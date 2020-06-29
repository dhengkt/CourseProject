#------------------------------------------------------------------------------
#
# nonPara_problem3.py
# nonparametric analysis homework problem three.
#
# This program will read two files provided by Professor Johnny Lin, and
# calculate the C.I for them by using the "t interval with bootstrap
# standard error" bootstrapping method.
#
# Create by HsinYu (Katie) Chi on 16 Feb. 2019
#
#------------------------------------------------------------------------------

#- Import:
import numpy as np
from scipy.stats import*
from scipy.stats import zscore

#- Function:
def problem3():

    # data from file "fat.dat.txt"
    # NOTE: Not sure what to put in other parameter to find exact values.
    less40 = np.genfromtxt("fat.dat.txt") #sample is younger than 40
    grea40 = np.genfromtxt("fat.dat.txt") #sample is older than 40

    # calculate the mean and standard deviation
    xBarles40 = np.mean(less40)
    xBargre40 = np.mean(grea40)

    # standard deviation
    les40std = np.std(less40)
    gre40std = np.std(grea40)

    # sample size
    n_less40 = np.size(less40)
    n_grea40 = np.size(grea40)

    # NOTE: I'm not sure if I need to replace the sample
    
    alpha = 0.05
    sigmaless40 = less40 - xBarles40
    sigmagrea40 = grea40 - xBargre40

    zscore = scipy.stats.zscore(0.05)

    E_less40 = zscore * (sigmaless40 / np.sqrt(n_less40))
    E_grea40 = zscore * (sigmagrea40 / np.sqrt(n_grea40))

    # CI for two set of data
    CI_upper_less40 = xBarles40 + E_less40
    CI_lower_less40 = xBarles40 - E_less40

    CI_upper_grea40 = xBargre40 + E_grea40
    CI_lower_grea40 = xBargre40 - E_grea40

    print("CI of under 40 yrs old : ( " , CI_upper_less40 , ", " , CI_lower_less40 + " )")
    print("CI of over 40 yrs old : ( " , CI_upper_grea40 , ", " , CI_lower_grea40 + " )")

    # NOTE: I'm not sure whether this calculation is correct or not.

#===== end file =====
