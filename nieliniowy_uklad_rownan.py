import numpy as np
import matplotlib.pyplot as plt


def func1(x):
    return -x**2 - x + 3


def func2(x):
    return np.divide(x**2, (1-x))


def func1p(x, y):
    return -np.sqrt(-y -x + 3)


def method():
    x = -1
    y = -1
    x_array = [x]
    y_array = [y]
    for i in range(20):
        xp = func1p(x, y)
        yp = func2(x)
        x, y = xp, yp
        x_array.append(x)
        y_array.append(y)
    return x_array, y_array, (x, y)


def dirrivatives(x, y):
    f1x = (2*x + 1)
    f1y = 1
    f2x = (2*x + y)
    f2y = (x - 1)
    return f1x, f1y, f2x, f2y


def jacob(f1x, f1y, f2x, f2y):
    J = f1x*f2y - f2x*f1y
    return J


def newton_rapson_method(x=0.5, y=1.5, t=500):
    x_array = [x]
    y_array = [y]
    for i in range(t):
        f1 = (-3 + x**2 + x + y)
        f2 = (x**2 + x*y - y)
        f1x, f1y, f2x, f2y = dirrivatives(x, y)
        J = jacob(f1x, f1y, f2x, f2y)
        xp = x - (f1*f2y - f2*f1y)/J
        yp = y - (f2*f1x - f1*f2x)/J
        x, y = xp, yp
        x_array.append(x)
        y_array.append(y)

    return x_array, y_array, (x, y)


def niceplot(title):
    plt.title(title)
    plt.ylabel("Y(x)")


x = np.linspace(-10, 10, num=1000, endpoint=False)
# graficzne rozwiązanie
gx1, gy1 = 2.2, -4.1
gx2, gy2 = -1.9, 1.2
gx3, gy3 = 0.7, 2.0
# obliczanie funkcji
y1 = func1(x)
y2 = func2(x)
# metoda iteracyjna
xa, ya, solution = method()
# metoda Newtona Raphsona
xr1, yr1, solutionr1 = newton_rapson_method(5, 8, 10000)
xr2, yr2, solutionr2 = newton_rapson_method(-2.5, 1, 1000)
xr3, yr3, solutionr3 = newton_rapson_method(0.5, 1.5, 500)

print("Rozwiązania metodą graficzną: ")
print("x1,y1 =", (gx1, gy1))
print("x2,y2 =", (gx2, gy2))
print("x3,y3 =", (gx3, gy3))
print("Metoda iteracyjna: " + str(solution))
print("Metoda Newtona_Rphsona: ")
print("x1,y1 =", solutionr1)
print("x2,y2 =", solutionr2)
print("x3,y3 =", solutionr3)
plt.subplot(2, 2, 1)
plt.plot(x, y1, x, y2, xa, ya, xa[-1], ya[-1], 'ro', xa[0], ya[0], 'yo')
label=['f1', 'f2', 'ścieżka do rozwiązania', 'punkt końcowy', 'punkt startowy']
niceplot("Metoda iteracyjna")
plt.subplot(2, 2, 2)
plt.plot(x, y1, x, y2, xr1, yr1, xr1[-1], yr1[-1], 'ro', xr1[0], yr1[0], 'yo')
niceplot("Metoda Newtona-Raphsona, 1 rozwiązanie")
plt.subplot(2, 2, 3)
plt.plot(x, y1, x, y2, xr2, yr2, xr2[-1], yr2[-1], 'ro', xr2[0], yr2[0], 'yo')
niceplot("Metoda Newtona-Raphsona, 2 rozwiązanie")
plt.subplot(2, 2, 4)
plt.plot(x, y1, x, y2, xr3, yr3, xr3[-1], yr3[-1], 'ro', xr3[0], yr3[0], 'yo')
niceplot("Metoda Newtona-Raphsona, 3 rozwiązanie")
plt.show()
