from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr
from sympy import lambdify

import numpy as np
import matplotlib.pyplot as plt

s = symbols("x")
p = parse_expr("sin(x*3.14)", evaluate=False)
f = lambdify("x", p)

lado_izquierdo = lambda f_lambda, x_a, x_b: f(f_lambda*x_a + (1 - f_lambda)*x_b) # Evaluación de las rectas
lado_derecho = lambda f_lambda, x_a, x_b: f_lambda*f(x_a) + (1 - f_lambda)*f(x_b) # Interpolación

def isConcava(left, right):
    return  left >= right

def isConvexa(left, rigth):
    return left <= rigth

def operation(x_a, x_b, lda):
    resultado = ""
    left = lado_izquierdo(lda, x_a, x_b)
    right = lado_derecho(lda, x_a, x_b)

    if (isConcava(left,right)):
        resultado = "La función es cóncava"
    elif (isConvexa(left,right)):
        resultado = "La función es convexa"
    else:
        resultado = "No se puede determinar"
    return left, right, resultado

if __name__ == "__main__":
    x_a = 0.25
    x_b = 2
    
    interpolation = []
    evaluation = []
    r = ""
    for lda in np.linspace(0,1):
        left, right, resultado = operation(x_a, x_b, lda)
        r = resultado
        print(resultado)
        interpolation.append(right)

    reverse = interpolation[::-1]

    x = np.linspace(0,3)
    x_1 = np.linspace(x_a,x_b)

    plt.figure(0)
    plt.title(resultado)
    plt.plot(x, f(x), color="k")
    plt.plot(x_1, f(x_1), color="b")
    plt.scatter(x_a, f(x_a), marker="o", c="red")
    plt.scatter(x_b, f(x_b), marker="o", c="red")
    plt.plot(x_1, reverse, color="r")
    #plt.plot(x_1,i, color="r")
    plt.show()