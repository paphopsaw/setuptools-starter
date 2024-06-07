from .myreference import ref_function
import numpy as np

def run_function():
    a = ref_function()
    b = np.ones(a.shape)
    return b