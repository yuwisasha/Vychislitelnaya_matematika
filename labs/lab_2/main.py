# f(x) = ln(x) - tg(x)

import math
import numpy as np

from labs.drawer import Drawer

TOL = 1e-4  # tolerance
MAX_ITERATIONS = 100


def f(x: float) -> float:
    y = math.log(x) - math.tan(x)

    return y


def muller_method(a: float, b: float, /) -> ...:
    k = 0
    x_k = (a + b) / 2

    while True:
        k += 1
        c = (a + b) / 2
        fa, fb, fc = f(a), f(b), f(c)
        A = (((fb - fc) / (b - c)) - ((fc - fa) / (c - a))) / (b - a)
        B = ((fc - fa) / (c - a)) + A * (a - c)
        C = fa

        x1 = a - ((2 * C) / (B + np.sqrt(B**2 - 4 * A * C)))
        x2 = a - ((2 * C) / (B - np.sqrt(B**2 - 4 * A * C)))

        if (a <= x1 <= b) or (a >= x1 >= b):
            x = x1
        elif (a <= x2 <= b) or (a >= x2 >= b):
            x = x2

        if fa * f(x) < 0:
            b = x
        elif f(x) * fb < 0:
            a = x

        E = abs(x - x_k)
        x_k = x

        if E <= TOL:
            print(f"x_k = {x}\nk = {k}\nf(x_k) = {f(x)}\nE = {E}")
            break


def main() -> None:
    x = np.arange(0.001, 10, 0.1)
    y = np.tan(x)
    x[:-1][np.diff(y) < 0] = np.nan
    y = np.log(x) - y

    drawer = Drawer(x, y)

    drawer.ylim = (-3, 3)
    drawer.xlim = (-10, 10)

    drawer.draw_graph()

    a, b = [  # left and right borders
        float(num)
        for num in input(
            "Введите начальное приближение через пробел: "
        ).split()
    ]

    muller_method(a, b)


if __name__ == "__main__":
    main()
