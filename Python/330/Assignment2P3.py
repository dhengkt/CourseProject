#=======================================================================
#                        General Documentation
#  Single-function module.
#
#  See function docstring for description.
#
#
#-----------------------------------------------------------------------
#                       Additional Documentation
#
#
# Modification History:
# - Jan 23, 2019. Original by HsinYu (Katie) Chi
#
# Notes:
# - Written for Assignment 2 Problem 3, Create a function distance that takes
#   a vector of x-locations and a vector of y-locations and calculates
#   the distance at all points defined by those locations from a given point.
#
# - I have problems when I want to avoid using loops to get this.
#=======================================================================

#-------------------- General Function:   Assignment2P3.py---------------------

import numpy as np
x = np.arange(5)
y = np.arange(4)
pt = np.array([-2.3, 3.3])
dist = []

for x_c in x:
    row = []
    for y_c in y:
        x_dist = (x_c + pt[0]**2)
        y_dist = (y_c + pt[0]**2)
        row.insert(0, (x_dist + y_dist)**(0.5))
        dist.insert(0, row)

print(dist)

#===== end file =====
