# f(x) = ln(x) - tg(x)

import numpy as np

from labs.drawer import Drawer

X = np.arange(0.001, 10, 0.1)
Y = np.tan(X)
Y[:-1][np.diff(Y) < 0] = np.nan
Y = np.log(X) - Y

E = 1e-4  # точность


def main() -> None:
    drawer = Drawer(X, Y)

    drawer.ylim = (-3, 3)
    drawer.xlim = (-10, 10)

    drawer.draw_graph()

    a, b = [
        float(num)
        for num in input(
            "Введите начальное приближение через пробел: "
        ).split()
    ]

    



if __name__ == "__main__":
    main()
