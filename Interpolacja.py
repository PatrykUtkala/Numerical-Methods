import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate


def calc_b(b, resp):
    if len(resp[0]) == 1:
        return [resp[1, 0]]
    else:
        bn1 = calc_b(b, resp[:, :-1])
        bn2 = calc_b(b, resp[:, 1:])
        return np.append(bn1, ((bn1[-1] - bn2[-1])/(resp[0, 0] - resp[0, -1])))


def func_interp_Newton_n(x, n, resp):
    b = []
    b = calc_b(b, resp)
    print("b=", b)
    a = 1
    f = b[0]*a
    for i in range(n-1):
        a *= x - resp[0, i]
        f += a*b[i+1]
    return f


def calculate_spline(x, resp):
    xi = resp[0]
    h = np.diff(resp[0])
    np.identity(len(resp()))
    print(xi, h)


with open('lab_8_dane/data7.txt', 'r') as f:
    response = [[float(num) for num in line.split()] for line in f]
response = np.transpose(response)

n = len(response[0])

x = np.linspace(-12, 8, num=1000)
y_newton = func_interp_Newton_n(x, n, response)
tck = interpolate.splrep(response[0], response[1], k=3)
y_spline = interpolate.splev(x, tck)
plt.plot(response[0], response[1], 'o', label="punkty trajektorii robota")
plt.plot(x, y_newton, 'r', label="fukcja interpolowana wielomianem Newtona")
plt.plot(x, y_spline, 'g--', label="funckja interpolowana metodą fukcji sklejanych 3 rzędu")
plt.ylabel('y')
plt.xlabel('x')
plt.legend()
plt.show()
