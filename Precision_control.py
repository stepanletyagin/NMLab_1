import math
import numpy as np
import Runge_Kutta_method as rkm

def Precision_control(system, initial_cond, start, stop, step, eps):
    N = math.floor((stop - start) / step)
    s = len(initial_cond)
    Y = np.zeros((N + 1, s))
    Y[0, :] = initial_cond
    T = np.zeros((N + 1, 1))
    T[0] = start
    for i in range(1, N + 1):
        step_curr = step
        while True:
            T1, Y1 = rkm.Runge_Kutta_method_step(system, T, Y, step_curr, i)
            T2, Y2 = rkm.Runge_Kutta_method_step(system, T, Y, step_curr / 2, i)
            if np.linalg.norm((Y1 - Y2), np.inf) / 15 < eps:
                break
            step_curr = step_curr / 2
        T = T1
        Y = Y1
    return T, Y