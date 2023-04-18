import matplotlib.pyplot as plt


def euler(g, t0, x0, dt, T):
    for _ in range(T):
        x0 += dt * g(t0, x0)
        t0 += dt
        yield [t0, x0]


def runge_kutt(g, t0, x0, dt, T):
    for _ in range(T):
        k1 = dt*g(t0, x0)
        k2 = dt*g(t0 + dt/2, x0 + k1/2)
        k3 = dt*g(t0 + dt/2, x0 + k2/2)
        k4 = dt*g(t0 + dt, x0 + k3)
        x0 += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t0 += dt
        yield t0, x0


def get_k0(alpha, s, A, lambda_, mu):
    return ((s*A)/(lambda_+mu))**(1/(1-alpha))


def solou(alpha, s, A, lambda_, mu):
    k0 = get_k0(alpha, s, A, lambda_, mu)
    print(k0)
    f = lambda t, k: -(lambda_ + mu) * k + s * A * pow(k, alpha)
    p1 = euler(f, 0, k0 + 5, 0.01, 1000)
    p2 = euler(f, 0, k0 - 5, 0.01, 1000)
    plt.plot(*zip(*p1))
    plt.plot(*zip(*p2))
    plt.plot([k0] * 10)
    plt.show()


lambda_ = 0.6
mu = 0.5
s = 0.8
A = 5
alpha = 0.4
solou(alpha, s, A, lambda_, mu)