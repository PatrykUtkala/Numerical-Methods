import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

t0 = 0
tk = 20
h = 0.03125
x0 = 5
y0 = 5
z0 = 5


def func(state):
    fx = -10 * state[0] + 10 * state[1]
    fy = 28 * state[0] - state[1] - state[0] * state[2]
    fz = -(8 / 3) * state[2] + state[0] * state[1]
    return np.array([fx, fy, fz])


def runge_kutty(t, init_state):
    x_array, y_array, z_array = [], [], []
    state = np.array(init_state)
    for t_now in t:
        k1 = func(state)
        k2 = func(state + k1 * (1 / 2) * h)
        k3 = func(state + k2 * (1 / 2) * h)
        k4 = func(state + k3 * h)
        state = state + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4) * h
        x_array.append(state[0])
        y_array.append(state[1])
        z_array.append(state[2])
    return np.array(x_array), np.array(y_array), np.array(z_array)


def init():
    line.set_data(x - xn, y - yn)
    line.set_3d_properties(z - zn)
    return line,


def animate(frame):
    i = np.sin(2 * np.pi * frame / 20000000)
    x, y, z = runge_kutty(t, [x0, y0, z0])
    xn, yn, zn = runge_kutty(t, [x0, y0, z0 + i])
    line.set_data(x, y)
    line.set_3d_properties(z - zn)
    return line,


t = np.arange(t0, tk, h)
print("steps: " + str(len(t)))
x, y, z = runge_kutty(t, [x0, y0, z0])
xn, yn, zn = runge_kutty(t, [x0 - 2, y0 + 1, z0 + 1])

fig = plt.figure()
ax = fig.add_subplot(221)
ax.plot(t, x, 'r', label="trajektoria x")
plt.ylabel('x')
plt.xlabel('t')
plt.legend()

ax = fig.add_subplot(222)
ax.plot(t, y, 'g', label="trajektoria y")
plt.ylabel('y')
plt.xlabel('t')
plt.legend()

ax = fig.add_subplot(223)
ax.plot(t, z, 'b', label="trajektoria z")
plt.ylabel('z')
plt.xlabel('t')
plt.legend()

ax = fig.add_subplot(224, projection='3d')
line, = ax.plot(x - xn, y - yn, z - zn, 'm', label="trajektoria fazowa")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
anim = FuncAnimation(fig, animate, init_func=init,
                     frames=2000000, interval=100, blit=True)
plt.show()
