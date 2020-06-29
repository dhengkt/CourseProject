# ----------------------------------------------------------------
#
# LinearAlgebra_problem2.py
# Linear Algebra and Statistics and Multiple Regression
#
# Code by HsinYu (Katie) Chi
# March 12 2019
#
# ----------------------------------------------------------------

alpha = 0.05
n = 20
p = 4


def overallF_test(ssr, sse, n, p):

    msr = ssr / (p-1)
    mse = sse / (n-p)
    f = msr / mse

    ssto = ssr + sse

    # NOTE: I am not sure how to calculate the p-value of this
    p_value = ()

    results = np.array(msr, mse, p_value, ssto, ssr, sse, f, n-1, n-p, p-1)

    return results

# ===== end file =====
