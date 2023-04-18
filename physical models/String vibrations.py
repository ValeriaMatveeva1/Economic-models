import matplotlib.pyplot as plt
import numpy as np


def strunka(u_0, dt, dx, a=1):
    ct = int(1 / dt) + 1
    cx = int(1 / dx) + 1
    u = [[0 for j in range(cx)] for i in range(ct)]
    l = (a * dt / dx) ** 2

    for i in range(cx):
        u[0][i] = u_0(dx * i)
        u[1][i] = u[0][i]

    for i in range(1, ct):
        u[i][0] = 0
    for i in range(1, ct):
        u[i][cx - 1] = 0

    for i in range(2, ct):
        for j in range(1, cx-1):
            u[i][j] = u[i-1][j]*2*(1-l)+l*(u[i-1][j+1]+u[i-1][j-1])-u[i-2][j]

    return u


u1 = strunka(lambda x: x*(1-x), 0.01, 0.03, 1)
for i in u1:
    plt.plot(i)
plt.show()

u2 = strunka(lambda x: x*(x*x-1), 0.01, 0.03, 1)
for i in u2:
    plt.plot(i)
plt.show()


def u3(x):
    if 0.2 <= x <= 0.3:
        return 3
    elif 0.7 <= x <= 0.8:
        return -2
    else:
        return 0


x = np.linspace(0, 1, 300)
y = np.vectorize(u3, otypes=[float])
graph1 = plt.plot(x, y(x))
plt.show()


