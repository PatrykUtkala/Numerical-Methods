import numpy as np
import matplotlib.pyplot as plt

# skrypt dokonuje obliczeń n-tego rozwinięcia w szereg potęgowy funkcji np.sin(x+np.pi/4)
# skrypt wykonuje wykresy przybliżeń funkcji na jednym wykresie
# widzimy że przy większym n szereg lepiej odwzorowuje zachowanie funkcji


def rozwiniecie(n, f):
    a = np.pi/4
    f_matrix = np.transpose(np.atleast_2d(f)) @ np.atleast_2d(np.ones(n))
    f_power = f_matrix ** np.arange(n)
    a1 = np.sin(a + np.pi*np.arange(n)/2)
    a2 = np.arange(n)
    a2[0] = 1

    a2 = np.cumprod(a2)
    print(a2)
    res = a1*f_power/a2
    res = np.sum(res, axis=1)
    return res


def plot_results():

    x = np.linspace(0, 1, num=100, endpoint=False)

    result = rozwiniecie(1, x)
    result1 = rozwiniecie(2, x)
    result2 = rozwiniecie(5, x)
    result3 = rozwiniecie(10, x)
    a = np.pi/4
    result_to_compare = np.sin(x+a)

    plt.plot(x, result_to_compare, 'r-', label='original')
    plt.plot(x, result, label='n=1')
    plt.plot(x, result1, label='n=2')
    plt.plot(x, result2, label='n=5')
    plt.plot(x, result3, label='n=10')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.legend()
    plt.show()


plot_results()
