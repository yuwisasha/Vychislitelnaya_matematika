# f(x) = ln(x) - tg(x)

import numpy as np
import matplotlib.pyplot as plt


def get_coefficients(_pl: int, _xi: np.ndarray):
    """
    Определение коэффициентов для множителей базисных полиномов l_i
    :param _pl: индекс базисного полинома
    :param _xi: массив значений x
    :return:
    """
    n = int(_xi.shape[0])
    coefficients = np.empty((n, 2), dtype=float)
    for i in range(n):
        if i == _pl:
            coefficients[i][0] = float("inf")
            coefficients[i][1] = float("inf")
        else:
            coefficients[i][0] = 1 / (_xi[_pl] - _xi[i])
            coefficients[i][1] = -_xi[i] / (_xi[_pl] - _xi[i])
    filtered_coefficients = np.empty((n - 1, 2), dtype=float)
    j = 0
    for i in range(n):
        if coefficients[i][0] != float("inf"):
            # изменение последовательности, степень увеличивается
            filtered_coefficients[j][0] = coefficients[i][1]
            filtered_coefficients[j][1] = coefficients[i][0]
            j += 1
    return filtered_coefficients


def get_polynomial_l(_xi: np.ndarray):
    """
    Определение базисных полиномов
    :param _xi: массив значений x
    :return:
    """
    n = int(_xi.shape[0])
    pli = np.zeros((n, n), dtype=float)
    for pl in range(n):
        coefficients = get_coefficients(pl, _xi)
        for i in range(1, n - 1):  # проходим по массиву coefficients
            if i == 1:  # на второй итерации занимаются 0-2 степени
                pli[pl][0] = coefficients[i - 1][0] * coefficients[i][0]
                pli[pl][1] = (
                    coefficients[i - 1][1] * coefficients[i][0]
                    + coefficients[i][1] * coefficients[i - 1][0]
                )
                pli[pl][2] = coefficients[i - 1][1] * coefficients[i][1]
            else:
                clone_pli = np.zeros(n, dtype=float)
                for val in range(n):
                    clone_pli[val] = pli[pl][val]
                zeros_pli = np.zeros(n, dtype=float)
                for j in range(n - 1):  # проходим по строке pl массива pli
                    product_1 = clone_pli[j] * coefficients[i][0]
                    product_2 = clone_pli[j] * coefficients[i][1]
                    zeros_pli[j] += product_1
                    zeros_pli[j + 1] += product_2
                for val in range(n):
                    pli[pl][val] = zeros_pli[val]
    return pli


def get_polynomial(_xi: np.ndarray, _yi: np.ndarray):
    """
    Определение интерполяционного многочлена Лагранжа
    :param _xi: массив значений x
    :param _yi: массив значений y
    :return:
    """
    n = int(_xi.shape[0])
    polynomial_l = get_polynomial_l(_xi)
    for i in range(n):
        for j in range(n):
            polynomial_l[i][j] *= _yi[i]
    L = np.zeros(n, dtype=float)
    for i in range(n):
        for j in range(n):
            L[i] += polynomial_l[j][i]
    return L


def affine_transform(a: float, b: float, N: int) -> list[float]:
    x = []

    for i in range(1, N+1):
        x_k = (1/2)*(a+b)+(1/2)*(b-a)*np.cos(((2*i - 1)/(2*N))*np.pi)
        x.append(x_k)

    return np.array(x)


def equation_from_list(lst: np.ndarray, x: np.ndarray) -> np.ndarray:
    res = []

    for i in x:
        y = 0
        for j in range(len(lst)):
            y += lst[j] * i**j
        else:
            res.append(y)

    return np.array(res)


def main() -> None:
    a, b = [
        float(i)
        for i in input(
            "Введите первоначальный отрезок интерполяции, два числа через пробел: "  # noqa
        ).split()
    ]

    N = int(input("Введите количество узлов: "))

    # original func
    x = np.arange(0.001, 10, 0.1)
    y = np.tan(x)
    x[:-1][np.diff(y) < 0] = np.nan
    y = np.log(x) - y

    # uniform nodes
    x_ = np.arange(a, b + ((b - a) / N), (b - a) / N)
    y_ = np.log(x_) - np.tan(x_)

    # Chebyshev nodes
    x__ = affine_transform(a, b, N)
    y__ = np.log(x__) - np.tan(x__)

    f1 = get_polynomial(x_, y_)
    f2 = get_polynomial(x__, y__)

    f1_y = equation_from_list(f1, x)
    f2_y = equation_from_list(f2, x)

    # draw funcs
    plt.plot(x, y)
    plt.plot(x, f1_y, "--o")
    plt.plot(x, f2_y, ":o")
    plt.legend(("f(x)", "Uniform", "Chebyshev"))
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
