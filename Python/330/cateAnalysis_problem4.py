#---------------------------------------------------------------------------
# cateAnalysis_problem4.py
# Compare the results of the SciPy chi2_contingency function 
# and SciPy's Fisher's exact test for the contingency table.
#
# Designed by HsinYu (Katie) Chi
# 05 March 2019
#---------------------------------------------------------------------------

#- Imports
import numpy as np
import time
from scipy.stats import chi2_contingency
from scipy.stats import fisher_exact

def main():

    start = time.time()

    a = np.array([[24329, 25345],[173342,174623]])
    print("Result of chi square: " + str(chi2_contingency(a)[1]))
    print("Result of fisher exact: " + str(fisher_exact(a, alternative='greater')))
    
    end = time.time()

    print("Times:" + str(end-start))

main()
