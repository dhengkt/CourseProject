#----------------------------------------------------------------
#
# LinearAlgebra_problem1.py
# Linear Algebra and Statistics and Multiple Regression
#
# Code by HsinYu (Katie) Chi
# March 12 2019
# 
# NOTE:This program is not finished.
#
#----------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt


# data from zyBooks
Y = [11.9, 22.8, 18.7, 20.1, 12.9, 21.7, 27.1, 25.4, 21.3, 19.3, 25.4, 27.2, 11.7, 17.8, 12.8, 23.9,
     22.6, 25.4, 14.8, 21.1]
X1 = [19.5, 24.7, 30.7, 29.8, 19.1, 25.6, 31.4, 27.9, 22.1, 25.5, 31.1, 30.4, 18.7, 19.7, 14.6, 29.5,
      27.7, 30.2, 22.7, 25.2]
X2 = [29.1, 28.2, 37, 31.1, 30.9, 23.7, 27.6, 30.6, 23.2, 24.8, 30, 28.3, 23, 28.6, 21.3, 30.1, 25.7,
      24.6, 27.1, 27.5]
X3 = [43.1, 49.8, 51.9, 54.3, 42.2, 53.9, 58.5, 52.1, 49.9, 53.5, 56.6, 56.7, 46.5, 44.2, 42.7, 54.4,
      55.3, 58.6, 48.2, 51]

B0 = 117.085
B1 = 4.334
B2 = -2.186
B3 = -2.857

Y_hat = np.array()

# draw the basic part of the graph.
plt.subplots(nrows=4, ncols=4, \
    sharex=True, sharey=True, squeeze=True, subplot_kw=None, gridspec_kw=None)



#===== end file =====
