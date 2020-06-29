#------------------------------------------------------------------------------
# Using the randomization (permutation) method, calculate the p-values for 
# pairwise groupings of the painkiller data in Example 3.5.1.
#
# nonparametric2
# nonPara2_problem3.py
# 
# Designed by HsinYu (katie) Chi
#
# NOTE:It might not working.
#------------------------------------------------------------------------------

#- Imports
import numpy as np
import random

#- Function

Placebo = [6, 4, 2, 2, 1]  # Placebo data
Aspirin = [4, 5, 6, 5, 6]  # Aspirin
NewPainkiller = [6, 5, 7, 8, 7]  # New Painkiller
alpha = 0.1/3
alpha2 = 0.05/3

Placebomean = np.mean(Placebo)
Aspirinmean = np.mean(Aspirin)
NewPainkillermean = np.mean(NewPainkiller)

averageMean = Placebomean - Aspirinmean - NewPainkillermean

data = np.concatenate(Placebo, Aspirin, NewPainkiller)
random.shuffle(data)
n_alldata = np.size(data)

# find the totally number of the average is over averageMean, and calculate
# the probability of obtaining.
templist = (Placebo + Aspirin + NewPainkiller)/3
total = 0

# NOTE: I'm not sure how to do the randomization with three sets of data,
# so I just guess it is like this.

for i in range(templist):
    if (templist[i] == averageMean or templist[i] > averageMean):
        total += 1
    else:
        total += 0

num = np.size(templist)
pro_of_obtain = total / num

if (pro_of_obtain > alpha):
    print("The results of alpha 1 are not statistically significant")
else:
    print("The results of alpha 1 are statistically significant")

if (pro_of_obtain > alpha2):
    print("The results of alpha 2 are not statistically significant")
else:
    print("The results of alpha 2 are statistically significant")

#===== end file =====
