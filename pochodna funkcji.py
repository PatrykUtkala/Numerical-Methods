import numpy as np
import matplotlib.pyplot as plt
import sys

# Skrypt oblicza przybliżenie pochonej funkcji f(0.5) = np.sin(x + np.pi / 4) dla różnych odległości h
# Na wykresie logarytmicznym widzimy spadek błędu ze zmniejszającym się h do pewnego momentu, potem błąd rośnie
# Zmniejszanie się błądu przy zwiększającej się dokładności jest dość intuicyjna ale wzrost błędu przy dalszej
# zwiększanej precyzji już niekoniecznie
# Może tak się dziać przez to, że przy małych odstępach między próbkami powstaje błąd dyskretyzacji
# wartości funkcji, wynik odejmowania ich odejmowania za szybko daje 0

len = 20


def function(x):
    fx = np.sin(x + np.pi / 4)
    return fx


def print_table(h, fpx, e):
    t = np.zeros((len, 4))
    t[:, 0] = np.arange(20)+1
    t[:, 1] = h
    t[:, 2] = fpx
    t[:, 3] = e
    print("[n|        h       |      f'(x)       |       e       ]")
    print(t)


def calculate():
    try:
        x = float(sys.argv[1]) * np.ones(len)
    except:
        x = 0.5 * np.ones(len)
    print(x[0])
    h = 0.4 * (0.2 * np.ones(len)) ** np.arange(len)

    fpx = (function(x + h) - function(x - h)) / (2 * h)
    tfpx = np.cos(x + np.pi / 4)
    e = np.abs(tfpx - fpx)

    print_table(h, fpx, e)

    plt.yscale('log')
    plt.xscale('log')
    plt.plot(h, e, 'r-o')
    plt.show()


calculate()
