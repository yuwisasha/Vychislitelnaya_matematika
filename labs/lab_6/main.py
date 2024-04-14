# f(x) = ln(x) - tg(x)

import numpy as np
import matplotlib.pyplot as plt

from typing import Callable


def trapz(f: Callable, a: float, b: float, N: int = 50):

    x = np.linspace(a, b, N + 1)  # N+1 points make N subintervals
    y = f(x)
    y_right = y[1:]  # right endpoints
    y_left = y[:-1]  # left endpoints
    dx = (b - a) / N
    T = (dx / 2) * np.sum(y_right + y_left)
    return T


def main() -> None:
    a, b = [
        float(i)
        for i in input(
            "Введите начало и конец отрезка, через пробел :"
        ).split()
    ]

    N = int(input("Введите количество узлов: "))

    f = lambda x: np.log(x) - np.tan(x)  # noqa

    x = np.arange(0.001, 10, 0.1)
    y = np.tan(x)
    x[:-1][np.diff(y) < 0] = np.nan
    y = np.log(x) - y

    x_ = np.linspace(a, b, N+1)
    y_ = f(x_)

    # draw
    plt.plot(x, y)
    plt.fill_between(x_, y_)
    axes = plt.gca()
    axes.spines["left"].set_position("center")
    axes.spines["bottom"].set_position("center")
    axes.spines["top"].set_visible(False)
    axes.spines["right"].set_visible(False)
    plt.grid()
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.show()


if __name__ == "__main__":
    main()
