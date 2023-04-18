import matplotlib.pyplot as plt
import math


def check(dx, dt, a):
    return dt/(dx*dx) <= 1/(2*a*a)


def u(u_0, dx, dt, u0=None, u1=None, a=1.):
    c = dt * (a / dx) ** 2
    if not check(dx, dt, a):
        raise ValueError()

    ct = int(1/dt)+1
    cx = int(1/dx)+1
    res = [[0 for j in range(cx)] for i in range(ct)]

    for j in range(cx):
        res[0][j] = u_0(dx*j)

    if u0 is not None:
        for i in range(1, ct):
            res[i][0] = u0
    if u1 is not None:
        for i in range(1, ct):
            res[i][cx-1] = u1

    for i in range(1, ct):
        for j in range(1, cx - 1):
            res[i][j] = res[i - 1][j] * (1 - 2 * c) + c * (res[i - 1][j + 1] + res[i - 1][j - 1])
        if u0 is None:
            res[i][0] = res[i][1]
        if u1 is None:
            res[i][cx-1] = res[i][cx-2]
    return res


def test_01():
    for i in u(lambda x: 100*x*(1-x), 0.01, 0.003, 0, 0, 0.1):
        plt.plot(i)
    plt.show()


def test_02():
    for i in u(lambda x: math.sin(1.5*math.pi*x), 0.01, 0.003, 0, 0, 0.1):
        plt.plot(i)
    plt.show()


def test_11():
    for i in u(lambda x: 100*x*(1-x), 0.01, 0.003, 0, None, 0.1):
        plt.plot(i)
    plt.show()


def test_22():
    for i in u(lambda x: math.sin(1.5*math.pi*x), 0.01, 0.003, None, None, 0.1):
        plt.plot(i)
    plt.show()


if __name__ == "__main__":
    test_01()
    test_02()
    test_11()
    test_22()
