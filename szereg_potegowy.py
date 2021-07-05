import numpy as np

# skrypt dokonuje obliczeń n-tego rozwinięcia w szereg potęgowy funkcji f(x) = np.sin(x+np.pi/4)
# skrypt wypisuje wyniki w postaci macierzy, w której 1 wiersz to numer rozwinięcia,
# 2 wiersz to wynik obliczeń, 3 wiersz to błąd bezwzględny, 4 wiersz to błąd względny


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


def table_of_results(x):
    results = np.zeros((4, 7))
    precision = np.array([1, 2, 3, 4, 5, 6, 10])
    for i in range(0, 7):
        results[1, i] = rozwiniecie(precision[i], x)
    results[0, :] = precision
    result_to_compare = np.sin(x+np.pi/4)
    results[2, :] = result_to_compare - results[1, :]  # błąd bezwzględny
    results[3, :] = (np.abs(results[2, :])/result_to_compare)*100  # błąd względny
    return results


def calculate():
    x = 0.99
    result = table_of_results(x)
    print(result)


calculate()
