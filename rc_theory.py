import matplotlib.pyplot as plt
import numpy as np
def f(t, v, r, c): #charge
    return v*(1-np.exp**-(t/(r*c)))
def g(t, v, r, c):
    return v*np.exp**-(t/(r*c))