import numpy as np


def pleasant_output(name, A, dim):
    print(name, '= ', end='')
    size = A.shape[0]
    if dim == 1:
        for j in range(size):
            print("{0:6.3f} ".format(A[j]), end='')
        print()
    else:
        for j in range(size):
            print("{0:6.3f} ".format(A[0, j]), end='')
        print()
        for i in range(1, size):
            print('    ', end='')
            for j in range(size):
                print("{0:6.3f} ".format(A[i, j]), end='')
            print()


# task 1
def get_coefficients(xij, Y):
    incr_proc = np.array((1.1, 1.5, 1.2))
    x = np.array(list(map(sum, xij)))
    X = Y + x
    print('GDP =', *X)
    A = xij / X
    X_incr = np.array(list(i[0] * i[1] for i in zip(incr_proc, X)))
    pleasant_output('A', A, 3)
    Y_incr = X_incr - x
    pleasant_output('Y_incr', Y_incr, 1)


xij = np.array(((150, 180, 80), (75, 270, 40), (25, 60, 40)))
Y = np.array((30, 25, 35))
get_coefficients(xij, Y)


# task 2
def get_GDP(A, Y):
    E = np.eye(3)
    pleasant_output('GDP', np.linalg.inv(E - A).dot(Y), 1)


A = np.array(((0.2, 0.1, 0.3), (0.1, 0.3, 0.2), (0.3, 0.2, 0.1)))
Y = np.array((155, 105, 40))
get_GDP(A, Y)
