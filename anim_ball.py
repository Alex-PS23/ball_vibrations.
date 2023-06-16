from math import pi
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def model(y, t):
    rho_w = 1000
    rho_b = 800

    r = 0.5
    V = (4 / 3) * pi * r * r * r
    m = rho_b * V
    eta = 4.220
    g = 9.8
    h0 = 10

    x, v = y

    if x < h0:
        dydt = [v, rho_w * g * V / m - 6 * pi * r * eta * v / m - g]
    else:
        dydt = [v, - g]

    return dydt


t_num = np.linspace(0, 60, 750)

y0 = [0.5, -5]

sol = odeint(model, y0, t_num)

x_ls = []
y_ls = []

fig = plt.figure()
fig.set_dpi(300)
fig.set_size_inches(5, 5)

ax = plt.axes(xlim=(-9.5, 9.5), ylim=(-5, 14))
ax.fill([-9.5, -9.5, 9.5, 9.5], [-30, 10, 10, -30])
patch = plt.Circle((0, 0), 1, fc='r')


def init():
    patch.center = (5, 5)
    ax.add_patch(patch)
    return patch,


def animate(i):
    x_ls.append(0)
    y_ls.append(sol[:, 0][i])

    patch.center = (0, y_ls[i])

    # ax.scatter(x, y)
    ax.set_xlim([-9.5, 9.5])
    ax.set_ylim([-5, 14])
    return patch,


# run the animation
ani = FuncAnimation(fig, animate, init_func=init,
                    frames=t_num.size,
                    interval=0.01, repeat=False)

print('Create calculate')
ani.save('animation.mp4', fps=60)
print('Create mp4')

plt.show()
