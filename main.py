import matplotlib.pyplot as plt
import Runge_Kutta_method as rkm
import SYSTEM as s
import Precision_control as PC
from config import *

T, Y = rkm.Runge_Kutta_method(s.system, initial_cond, start, stop, step)
T1, Y1 = PC.Precision_control(s.system, initial_cond, start, stop, step, eps)
fig = plt.figure()
plt.plot(Y[:, 0], Y[:, 1])
plt.grid()
plt.show()
fig = plt.figure()
plt.plot(Y1[:, 0], Y1[:, 1])
plt.grid()
plt.show()
fig.savefig('saved_figure.jpg')
# print(T, Y)