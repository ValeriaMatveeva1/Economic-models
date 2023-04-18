import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D


def progonka(a, b, c, f):
    n = len(f)
    alpha = [0 for _ in range(n)]
    beta = [0 for _ in range(n)]
    x = [0 for _ in range(n)]

    for i in range(1, n - 1):
        alpha[i] = (b[i] / (- a[i] * alpha[i - 1] - c[i]))
        beta[i] = ((- f[i] + a[i] * beta[i - 1]) / (- a[i] * alpha[i - 1] - c[i]))
    alpha[n - 1] = 0
    beta[n - 1] = (- f[n - 1] + a[n - 1] * beta[n - 2]) / (- a[n - 1] * alpha[n - 2] - c[n - 1])

    x[n - 1] = beta[n - 1]
    for i in range(n - 1, 0, -1):
        x[i - 1] = alpha[i - 1] * x[i] + beta[i - 1]

    return x


t = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
x = [0, 0.2, 0.4, 0.6, 0.8, 1]
a=[0, 2.5, 2.5, 2.5, 2.5, -1]
b=[0, 2.5, 2.5, 2.5, 2.5, 0]
c=[1, -6, -6, -6, -6, 1]
y = progonka(
    [0, 2.5, 2.5, 2.5, 2.5, -1],
    [0, 2.5, 2.5, 2.5, 2.5, 0],
    [1, -6, -6, -6, -6, 1],
    [0, -0.16, -0.24, -0.24, -0.16, 0])
xx = y.copy()
res = [[0, 0.16, 0.24, 0.24, 0.16, 0], xx]
y[-1] = 0
for i in range(9):
    y = progonka(a, b, c, [-i for i in y])
    xx = y.copy()
    res.append(xx)
    y[-1] = 0

def draw_3d(_res):
    _res = np.array(_res)
    n, m = len(res), len(res[0])
    _x = np.linspace(0, 1, m)
    _y = np.linspace(0, 1, n)
    xx, yy = np.meshgrid(_x, _y)
    print(xx, yy)
    ax = plt.axes(projection='3d')
    ax.plot_surface(xx, yy, np.array(_res))
    plt.show()

draw_3d(res)
