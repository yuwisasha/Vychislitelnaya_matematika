# func 16

import numpy as np


def TDMA(
    a: list[int | float],
    b: list[int | float],
    c: list[int | float],
    f: list[int | float],
) -> list[int | float]:
    a, b, c, f = tuple(
        map(lambda k_list: list(map(float, k_list)), (a, b, c, f))
    )

    alpha = [-b[0] / c[0]]
    beta = [f[0] / c[0]]
    n = len(f)
    x = [0] * n

    for i in range(1, n):
        alpha.append(-b[i] / (a[i] * alpha[i - 1] + c[i]))
        beta.append((f[i] - a[i] * beta[i - 1]) / (a[i] * alpha[i - 1] + c[i]))

    x[n - 1] = beta[n - 1]

    for i in range(n - 1, -1, -1):
        x[i - 1] = alpha[i - 1] * x[i] + beta[i - 1]

    return [round(i) for i in x]


def main() -> None:

    arr = np.loadtxt("labs/lab_4/input.txt", dtype="i", delimiter=",")
    x = arr[:, 4].copy()
    arr = np.delete(arr, 4, 1)

    b = np.diag(arr, k=1)  # superdiagonal
    c = np.diag(arr)  # diagonal
    a = np.diag(arr, k=-1)  # subdiagonal

    b = np.append(b, 0)
    a = np.insert(a, 0, 0)

    print(f"input matrix =\n{arr}\nx = {x}")

    print(f"result = {TDMA(a=a, b=b, c=c, f=x)}")


if __name__ == "__main__":
    main()
