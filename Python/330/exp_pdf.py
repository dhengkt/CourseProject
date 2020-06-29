import numpy as np
from scipy import quan

def mexp(x, mylambda = 0.1):
    return mylambda * np.exp(-mylambda * x)
