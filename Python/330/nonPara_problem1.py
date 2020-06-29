#------------------------------------------------------------------------------
#
# nonPara_problem1.py
# non-parametric analysis homework problem one.
#
# This program will read two files provided by Professor Johnny Lin, and
# compare whether the data are the same with different calculation.
#
# Create by HsinYu (Katie) Chi on 16 Feb. 2019
# NOTE: I do not know how to do some part of the problem, so this program is not
# complete.
#
#------------------------------------------------------------------------------

#- Import:
import numpy as np
from scipy.stats import t

#- Function
def compare_two_data():

    # Data from fat.dat.txt file
    data_Brozek = np.genfromtxt("fat.dat.txt",delimiter=[10,11,12,13])
    data_Siri = np.genfromtxt("fat.dat.txt", delimiter=[18, 19, 20, 21])

    # Hypotheses should be
    # mu0: mean of the Brozek data should be the same as Siri's data
    # mu1: mean of the Brozek data and Siri data are not the same

    # Calculate the test statistic for the original data
    xBarBroz = np.mean(data_Brozek)
    xBarSiri = np.mean(data_Siri)
    differenceBetween = xBarBroz - xBarSiri

    # Find all the possible way to calculate the difference
    # NOTE: I do not know how to do this part.

    # After finding all the possible differences, calculate the possibiliy of
    # it and check whether it's in 0.05 or not.
    alpha = 0.05
    #totaldiff =

    # find the totally number of the differences
    numDiff = np.size()
    #print((alpha = totalDiff / numDiff))

    #- Solution from professor Johnny Lin
    #raw_data = np.genfromtxt("fat.dat.txt")
    #brozek = raw_data[:,1]
    #siri = raw_data[:,2]
    #data = np.comcatenate((brozek,siri))

    #n_group = np.size(brozek)

    #results = np.zeros(10000, dtype='d')
    #for i in range(np.size(results)):
    #   np.random.shuffle(data)
    #   results[i] = np.mean(data[:n_group]) - np.mean(data[-n_group:])

    #diff_orig = np.mean(brozek) - np.mean(siri)
    #p_value_orig = np.sum(np.absolute(results) >= abs(diff_orig)) / np.size(results)


#===== end file =====
