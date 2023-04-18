import matplotlib.pyplot as plt


def runge_kutt_solve_system(g, f, t0, x0, y0, dt, T):
    for _ in range(T):
        k1_x = dt * g(t0, x0, y0)
        k1_y = dt * f(t0, x0, y0)

        k2_x = dt * g(t0 + dt / 2, x0 + k1_x / 2, y0 + k1_y / 2)
        k2_y = dt * f(t0 + dt / 2, x0 + k1_x / 2, y0 + k1_y / 2)

        k3_x = dt * g(t0 + dt / 2, x0 + k2_x / 2, y0 + k2_y / 2)
        k3_y = dt * f(t0 + dt / 2, x0 + k2_x / 2, y0 + k2_y / 2)

        k4_x = dt * g(t0 + dt, x0 + k3_x, y0 + k3_y)
        k4_y = dt * f(t0 + dt, x0 + k3_x, y0 + k3_y)

        x0 += (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        y0 += (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
        t0 += dt

        yield x0, y0


a = 3  # коэффициент рождаемости жертв
b = 2  # коэффициент смертности жертв
c = 1.8  # коэффициент смертности хищников
d = 1  # коэффициент рождаемости хищников
dtx = lambda t, x, y: a * x - b * x * y
dty = lambda t, x, y: -c * y + d * y * x
res = []
for i in runge_kutt_solve_system(dtx, dty, 0, 3, 1, 0.01, 1000):
    res.append(i)

plt.plot(res, label={'Жертвы', 'Хищники'})
plt.legend()
plt.xlabel('Время')
plt.ylabel('Популяции')
plt.show()

sp = (c/d, a/b)
plt.scatter(*sp, label=f'стац. т-ка: x={sp[0]}, y={sp[1]}')
res_x = []
res_y = []
for i, j in runge_kutt_solve_system(dtx, dty, 5, 10, 2, 0.01, 1000):
    res_x.append(i)
    res_y.append(j)

plt.plot(res_x, res_y)
plt.show()


