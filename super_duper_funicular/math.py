"""
math operations
"""
import numpy as np
# add : adds two value
def add (x,y):
    """
    add : adds two value
    """
    return x+y

def mult (x, y):
    """
    multiply : 2 values
    """
    return x * y

def sqrt (x):
    """
    Find the square root of x
    if x <= 0, the function will return 0 
    """
    if x > 0:
        return np.sqrt(x)
    else :
        return 0;


