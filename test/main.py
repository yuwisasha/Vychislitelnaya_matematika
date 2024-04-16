import csv
import numpy as np
import matplotlib.pyplot as plt

# Параметры
omega = 1.0  # Частота осцилляций
T = 10.0  # Время окончания расчета
dt = 0.1  # Шаг по времени
timesteps = int(T / dt)  # Количество временных шагов

# Начальные условия
y0 = 1.0  # y(0)
y_prime0 = 0.0  # y'(0)

# Массивы для хранения значений
t_values = np.linspace(0, T, timesteps + 1)  # Массив значений времени
y_analytical = y0 * np.cos(omega * t_values) + y_prime0 / omega * np.sin(omega * t_values)  # Аналитическое решение
y_numerical = np.zeros_like(t_values)  # Численное решение

# Вычисление численного решения методом конечных разностей
y_numerical[0] = y0
y_numerical[1] = y_numerical[0] + dt * y_prime0
for i in range(2, timesteps + 1):
    y_numerical[i] = 2 * y_numerical[i-1] - y_numerical[i-2] - (dt ** 2) * omega ** 2 * y_numerical[i-1]

# Вывод результатов
print("Таблица значений функции:")
print("t\tАналитическое решение\tЧисленное решение")
for t, y_analytic, y_numeric in zip(t_values, y_analytical, y_numerical):
    print(f"{t:.1f}\t{y_analytic:.3f}\t\t\t{y_numeric:.3f}")

with open("solution.csv", "w", newline="") as csvfile:
    fieldnames = ["t", "Аналитическое решение", "Численное решение"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for t, y_analytic, y_numeric in zip(t_values, y_analytical, y_numerical):
        writer.writerow({"t": t, "Аналитическое решение": y_analytic, "Численное решение": y_numeric})

# Графическое представление
plt.figure(figsize=(10, 6))
plt.plot(t_values, y_analytical, label="Аналитическое решение", linestyle='--', color='blue')
plt.plot(t_values, y_numerical, label="Численное решение", marker='o', linestyle='-', color='red')
plt.xlabel('Время')
plt.ylabel('y')
plt.title('Численное и аналитическое решение уравнения гармонического осциллятора')
plt.legend()
plt.grid(True)
plt.show()
