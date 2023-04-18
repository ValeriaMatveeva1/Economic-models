import matplotlib.pyplot as plt


def runge_kutt_solve_system(g, f, h, t0, x0, y0, z0, dt, T):
    for _ in range(T):
        k1_x = dt * g(t0, x0, y0, z0)
        k1_y = dt * f(t0, x0, y0, z0)
        k1_z = dt * h(t0, x0, y0, z0)

        k2_x = dt * g(t0 + dt / 2, x0 + k1_x / 2, y0 + k1_y / 2, z0 + k1_z / 2)
        k2_y = dt * f(t0 + dt / 2, x0 + k1_x / 2, y0 + k1_y / 2, z0 + k1_z / 2)
        k2_z = dt * h(t0 + dt / 2, x0 + k1_x / 2, y0 + k1_y / 2, z0 + k1_z / 2)

        k3_x = dt * g(t0 + dt / 2, x0 + k2_x / 2, y0 + k2_y / 2, z0 + k2_z / 2)
        k3_y = dt * f(t0 + dt / 2, x0 + k2_x / 2, y0 + k2_y / 2, z0 + k2_z / 2)
        k3_z = dt * h(t0 + dt / 2, x0 + k2_x / 2, y0 + k2_y / 2, z0 + k2_z / 2)

        k4_x = dt * g(t0 + dt, x0 + k3_x, y0 + k3_y, z0 + k3_z / 2)
        k4_y = dt * f(t0 + dt, x0 + k3_x, y0 + k3_y, z0 + k3_z / 2)
        k4_z = dt * h(t0 + dt, x0 + k3_x, y0 + k3_y, z0 + k3_z / 2)

        x0 += (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        y0 += (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
        z0 += (k1_z + 2 * k2_z + 2 * k3_z + k4_z) / 6
        t0 += dt

        yield x0, y0, z0


a = 10
b = 2.67
r = 24
dtx = lambda t, x, y, z: -a * x + a * y
dty = lambda t, x, y, z: r * x - y - x * z
dtz = lambda t, x, y, z: -b * z + x * y
res = []
for i in runge_kutt_solve_system(dtx, dty, dtz, 0, 20, 20, 20, 0.01, 5000):
    res.append(i)

plt.plot(res, label={'X', 'Y', 'Z'})
plt.legend()
plt.xlabel('Время')
plt.ylabel('Параметры')
plt.show()

res_x = []
res_y = []
res_z = []
for i, j, n in runge_kutt_solve_system(dtx, dty, dtz, 0, 20, 20, 20, 0.01, 5000):
    res_x.append(i)
    res_y.append(j)
    res_z.append(n)
plt.plot(res_x, res_y)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
plt.plot(res_y, res_z)
plt.xlabel('Y')
plt.ylabel('Z')
plt.show()
plt.plot(res_x, res_z)
plt.xlabel('X')
plt.ylabel('Z')
plt.show()