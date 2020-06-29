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
# - Written for Assignment 2 Problem 4, drawing a sine wave from
#   0 to 2pi, use at least 15 opints
#=======================================================================

#-------------------- General Function:   Assignment2P4.py---------------------

import numpy as np
import matplotlib.pyplot as plt

radians = np.arange(0,2*np.pi,0.5)  # Set the radians from 0 to 2pi
y = np.sin(radians)                 # Set y = sin(radians)
plt.plot(radians,y, color="blue")   # Set the graph one for normal line
plt.plot(radians,y, 'bo')           # Second graph for showing the opints
plt.xlabel("Radians")               # Set the label of x-axis
plt.ylabel("Sine")                  # Set the label of y-axis
plt.show()                          # Show the graph
plt.savefig("SineWave")             # Save the image with name "SineWave"

#===== end file =====
