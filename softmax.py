import numpy as np

def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    return [x * 1.0 / sumExpL for x in expL]