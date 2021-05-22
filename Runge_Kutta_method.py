import math
import numpy as np

def Runge_Kutta_method(system, initial_cond, start, stop, step):
    N = math.floor((stop - start) / step)
    s = len(initial_cond)
    Y = np.zeros((N + 1, s))
    Y[0, :] = initial_cond
    T = np.zeros((N + 1, 1))
    T[0] = start
    for i in range(1, N + 1):
    # while T[i - 1] < stop:
        # T[i] = T[i - 1] + step
        # k_1 = system(T[i - 1], Y[i - 1, :])
        # k_2 = system(T[i - 1] + step/2, Y[i - 1, :] + k_1 * step/2)
        # k_3 = system(T[i - 1] + step/2, Y[i - 1, :] + k_2 * step/2)
        # k_4 = system(T[i - 1] + step, Y[i - 1, :] + k_3 * step)
        # Y[i, :] = Y[i - 1, :] + step/6 * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
        T, Y = Runge_Kutta_method_step(system, T, Y, step, i)
    return T, Y

def Runge_Kutta_method_step(system, T, Y, step, i):
    T[i] = T[i - 1] + step
    k_1 = system(T[i - 1], Y[i - 1, :])
    k_2 = system(T[i - 1] + step / 2, Y[i - 1, :] + k_1 * step / 2)
    k_3 = system(T[i - 1] + step / 2, Y[i - 1, :] + k_2 * step / 2)
    k_4 = system(T[i - 1] + step, Y[i - 1, :] + k_3 * step)
    Y[i, :] = Y[i - 1, :] + step / 6 * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
    return T, Y