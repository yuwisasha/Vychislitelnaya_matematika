# f(x) = ln(x) - tg(x)

import math
import numpy as np

from labs.drawer import Drawer

TOL = 1e-4  # tolerance
MAX_ITERATIONS = 1000


def f(x: float) -> float:
    # print(x)
    y = math.log(x) - math.tan(x)

    return y


def muller_method(left: float, center: float, right: float, /) -> ...:
    x0, x1, x2 = left, right, center

    h1 = x1 - x0
    h2 = x2 - x1
    e1 = (f(x1) - f(x0)) / h1
    e2 = (f(x2) - f(x1)) / h2
    d = (e2 - e1) / (h2 + h1)
    k = 2

    while k <= MAX_ITERATIONS:
        b = e2 + h2 * d
        D = (b**2 - 4 * f(x2) * d) ** 1 / 2

        if abs(b - D) < abs(b + d):
            E = b + D
        else:
            E = b - D

        h = -2 * f(x2) / E
        p = x2 + h

        if abs(h) < TOL:
            # print(p, k, f(p), E)
            print(f"x(k) = {p}\nk = {k}\nf(x(k)) = {f(p)}\nE = {TOL}")
            return

        x0 = x1
        x1 = x2
        x2 = p
        h1 = x1 - x0
        h2 = x2 - x1
        e1 = (f(x1) - f(x0)) / h1
        e2 = (f(x2) - f(x1)) / h2
        d = (e2 - e1) / (h2 - h1)
        k += 1


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

    muller_method(a, (a + b) / 2, b)


if __name__ == "__main__":
    main()
