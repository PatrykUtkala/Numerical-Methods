import numpy as np
import scipy.integrate as integrate

def func(x):
    w = np.array([-0.03421, 0.4325, -0.4531, 2.42, 5.1])
    pot = np.flip(np.arange(5))
    x = np.transpose(x)
    x = np.transpose(np.array([x, x, x, x, x]))
    return np.sum((w * (x ** pot)), axis=1)


def trapezy(x, y):
    podstawy = np.diff(x)
    return np.sum((y[:-1] + y[1:]) * podstawy / 2)


w = np.array([-0.03421, 0.4325, -0.4531, 2.42, 5.1])
p = [-6, 12]
pot = np.flip(np.arange(5) + 1)
wp = w / pot
wynik = np.sum(wp * (p[1] ** pot) - wp * (p[0] ** pot))
print("Wynik liczenia analitycznie", wynik)

x1 = np.linspace(p[0], p[1], num=3)
x2 = np.linspace(p[0], p[1], num=5)
x3 = np.linspace(p[0], p[1], num=9)
x4 = np.linspace(p[0], p[1], num=17)
y1 = func(x1)
y2 = func(x2)
y3 = func(x3)
y4 = func(x4)

t1 = trapezy(x1, y1)
t2 = trapezy(x2, y2)
t3 = trapezy(x3, y3)
t4 = trapezy(x4, y4)

wr1 = t2 * (4 / 3) - t1 * (1 / 3)
wr2 = t3 * (4 / 3) - t2 * (1 / 3)
wr3 = t4 * (4 / 3) - t3 * (1 / 3)
wrr1 = wr2 * (16 / 15) - wr1 * (1 / 15)
wrr2 = wr3 * (16 / 15) - wr2 * (1 / 15)
wynik_Romberg = wrr2 * (64 / 63) - wrr1 * (1 / 63)
print("wynik metody Romberga:", wynik_Romberg, "błąd[%]:", ((wynik - wynik_Romberg) / wynik) * 100)

wynik_kwadratury = integrate.fixed_quad(func, p[0], p[1], n=3)[0]
print("wynik kwadratury Gaussa:", wynik_kwadratury, "błąd[%]:", ((wynik - wynik_kwadratury) / wynik) * 100)
# śmiesznie wyszło że obydwie metody mają taki sam błąd
