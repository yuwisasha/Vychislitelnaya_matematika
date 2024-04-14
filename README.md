# Repo for "computational mathematics" labs

## Launch
```
git clone https://github.com/yuwisasha/Vychislitelnaya_matematika.git
```
```
poetry install
```
```
python -m labs.lab_{choose from 1 to 6}.main
```

### Lab 1
#### Draw graphs
Drawer class in drawer.py, which helps to draw functions using **matplotlib**. Draws an analytically defined function $f(x) = sin(x)$ or table defined function from *table_defined_func.csv*

### Lab 2
#### Solving a nonlinear equation
$$f(x) = ln(x) - tan(x)$$

* Method: **Parabola method**(**Muller's metod**).

Graphically find segmemt like [4.1, 4.7] on the graph and set them in the program input

### Lab 3
#### Minimization of a function with one variable
$$f(x) = ln(x) - tan(x)$$

* Method: **Newton's method**

Set the initial approximation to the root, like 4.3, it finds a root with TOL(tolerance) <= $10^4$

### Lab 4
#### Linear algebra problems
Table defined func in *input.txt*:

|2|-1|0|0|
|-|-|-|-|
|-1|2|-1|0|
|0|-1|2|-1|
|0|0|-1|2|

and free term column

|2|
|-|
|2|
|2|
|17|

* Method: **Triadiagonal method**(**Thomas algorithm**)

### Lab 5
#### Function approximation 

$$f(x) = ln(x) - tg(x)$$

* Method: **Interpolation Lagrange method**(**ILM**)

Graphically find segmemt with from 1 to 3 extremums on the graph and set them in the program input with number of steps. Programm will draw initial func, 2 funcs based on ILM, first has a constant step, and second has a **Chebyshev** nodes.

### Lab 6
#### Numerical integration

$$f(x) = ln(x) - tg(x)$$

* Method: **Trapezoid method**

Inputs segment [a, b], which you want integrate, and number of steps in segment - N. Draws a graph and a filled trapezoid(integrated segment).






