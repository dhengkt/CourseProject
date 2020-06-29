#-----------------------------------------------------------------------------
# Program to solve a cars problem using Kruskal-Wallis.
#
# nonparametric2
# nonPara2_problem2.py
#
# Designed by HsinYu (Katie) Chi
#
#-----------------------------------------------------------------------------

#- Imports

import numpy as np
from scipy.stats import kruskal
from scipy.stats import chi2

#- Data
#data from zyBooks Table 3.4.1

Placebo = [6, 4, 2, 2, 1]       #Placebo data
Aspirin = [4, 5, 6, 5, 6]       #Aspirin
NewPainkiller = [6, 5, 7, 8, 7] #New Painkiller
alpha = 0.02

allData = np.concatenate((Placebo, Aspirin, NewPainkiller))
allData.sort()
n = np.size(allData)

ranking = []
for i in range(n):
    if (allData[i] != allData[i+1]):
        ranking = i + 1
    else:
        # this part has to calculate the average of the ranking for 
        # repeated numbers.
        ranking = i

# calculate the sum of r for each group
R_for_Placebo = np.sum(np.where(allData == Placebo, ranking, 0.0))
R_for_Aspirin = np.sum(np.where(allData == Aspirin, ranking, 0.0))
R_for_NewPainkiller = np.sum(np.where(allData == NewPainkiller, ranking, 0.0))

H = (12/(n*(n+1))) * ((R_for_Placebo/5) +
                      (R_for_Aspirin/5)+(R_for_NewPainkiller/5)) - 3 * (n+1)

g = 3  # number of groups
df = g - 1  # degrees of freedom
h_statistic, scipy_p_value = kruskal(Placebo, Aspirin, NewPainkiller)
p_value = 1.0 - chi2.cdf(h_statistic, df)

#- Print results
print("H-statistic: " + h_statistic)
print("SciPy kruskal p-value: " + scipy_p_value)
print("My p-value: " + p_value)
print("Reject H0?: " + (scipy_p_value < alpha))

#==== end file =====
