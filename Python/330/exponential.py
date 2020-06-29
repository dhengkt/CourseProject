#-----------------------------------------------------------------------
#                       Additional Documentation
#
# Modification History:
# - 16 Jan 2019:  Original by HsinYu (Katie) Chi
#
# Notes:
# - Written for Python 3.7.2
# - Module docstrings can be tested using the doctest module.  To
#   test, execute "python exponential.py".
# - See import statements throughout for more information on non-
#   built-in packages and modules required.
#=======================================================================

#---------------- Module General Import and Declarations ---------------

#- Set module version number etc. to package version number etc.:
#
#import package
#math

#-------------------- General Function:  exponential ---------------------

from math import*

#Taking the x and tol to calculate the exponential function.
def exponential(x,tol):
    return expo(x,100,tol)


#Helper functions help calculate the sum of all values.
def expo(x, n, tol):
    if n == 0:
        return 1
    return x**n / factorial(n) + expo(x, n-1, tol)

#Test the exponential function with some cases.
def main():

    print(exponential(1, 1e-8))
    print(exponential(3.4, 1e-8))

main()

#===== end file =====
