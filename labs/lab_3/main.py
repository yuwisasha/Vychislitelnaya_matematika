import math

MAX_ITERATIONS = 1e3
E = 1e-4
F = lambda x: math.log(x) - math.tan(x)  # noqa 
F_1 = lambda x: (1 / x) - (1 / math.cos(x) ** 2)  # noqa 1st derivateive
F_2 = lambda x: -(2 * math.sin(x)) / (math.cos(x) ** 3) - (1 / x**2)  # noqa 2nd derivative


def newton(x: float) -> None:
    x_a = x
    k = 0

    while True and k <= MAX_ITERATIONS:
        print(x, x_a)
        k += 1
        x = x_a - F_1(x_a) / F_2(x_a)
        if abs(x - x_a) < E:
            print(
                f"x_k = {x}\nk = {k}\nf(x_k) = {F(x)}\nf'(x_k)={F_1(x)}\nE = {E}"  # noqa
            )
            break
        x_a = x


def main() -> None:
    x = float(input("Задайте начальное приближение: "))

    newton(x)


if __name__ == "__main__":
    main()
