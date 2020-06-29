#ParaAnalysisP2.py
#HsinYu (Katie) Chi

import numpy as np
from scipy import stats

def findXBar(datalist):
    # using loop to generate the x bar value
    for i in range (len(datalist)):
        sumOfX += datalist[i]
    return sumOfX

def findStandardD(x_Bar, datalist):
    # using loop to generate the standard deviation
    sum = 0

    for i in range (len(datalist)):
        f = datalist[i] - x_Bar
        sum += f
    StandardD = np.sqart(sum / (len(datalist)-1))
    return StandardD

def solveproblem(datalist, mu):

    sumOfx = findXBar(daatlist)
    x_bar = sumOfx / (len(datalist))

    standardD = findStandardD(x_bar, datalist)

    tstatis = (x_bar - mu) / (standardD / np.sqrt(len(datalist) - 1))

    mu1 = x_bar - tstatis
    mu2 = x_bar + tstatis

    return print(mu1, mu2)

def main():

    datalist = [7.72, 9.58, 12.38, 7.77, 11.27, 8.80, 11.10, 7.80, 10.17, 6.00]
    mu = 30
    solveproblem(datalist, mu)

main()

#===== end file =====
