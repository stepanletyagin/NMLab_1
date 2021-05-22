from config import *
import numpy as np

def system(t, y):
    F = np.zeros(eq_num)
    F[0] = (1 - y[0]) * y[0] * y[0] / (n + y[0]) - y[1] * y[0]
    F[1] = gamma * (y[0] - m) * y[1]
    return F