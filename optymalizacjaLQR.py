import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg


a2 = -2.7
a1 = 1.8
a0 = -0.25
n_max = 20000
dt = 0.001
c1 = 1
c2 = 1.08
A = np.array([[-a2, -a1, -a0],
              [1, 0, 0],
              [0, 1, 0]], dtype=float)

B = np.array([[1], [0], [0]], dtype=float)
C = np.array([1, 1, 1], dtype=float)
D = 0
x = np.array([[0], [0], [0]], dtype=float)
u = 1
u_array = []
y = []

Q = np.identity(3)*c1
P = linalg.solve_continuous_are(A, B, Q, c2)

# F = np.linalg.inv(c2 + (np.transpose(B) @ P @ B)) @ np.transpose(B) @ P @ A
K = (1/c2)*np.transpose(B) @ P  # użyta wersja ciągłoczasowa
A = A - (B @ K)
print("Układ nie jest stabilny, ma 3 niestabilne pierwiastki")
print("stosunek c1 do c2 wpływa na parametry ustabilizowanej fukcji(czas narastania, uchyb w stanie ustalonym itd.")
print("Wykres niebieski to wysterowany sygnał a wykres czerwony przerywany to sygnał sterujący")
for n in range(n_max):
    xp = A @ x + B * u
    yp = np.atleast_2d(C) @ np.atleast_2d(x) + np.atleast_2d(D) * u
    y.append(yp)
    u_array.append(-K@x)
    x += xp * dt
n = np.arange(n_max)
plt.plot(n, np.reshape(y, n_max), n, np.reshape(u_array, n_max), 'r--')
plt.show()
