import numpy as np
import matplotlib.pyplot as plt


respuesta = ""


def f_x(x):
    return x**2


# def f_x(x):
    return 3*x**2+x-3


# def f_x(x):
    return 2*x**3+2*x**2+x


def comprobar(x_a, x_b, lamda):
    aux = ""


def graficar_fx(xa, xb):
    x = []
    result = []
    for i in np.arange(xa*1.2, xb*1.2, 0.1):
        x. append(i)
    for i in x:
        result.append(fx(i))

    return plt.plot(x, result, color="black", label="f(x)")


def graficaRecta(x_a, x_b):
    X = пр.arange(x_а, х_b, 2)
    y = (f_x(x_a), f_x(x_b))
    return plt.plot(x, y, color="red", linewidth=3)


def izquierda(x_a, x_b, aux):
    X = []
    res = []
    for i in np.arange(x_a, x_b, step=0.1):
        х.арpend(i)
        res.append(fx(aux*i + (1-aux) i))  # fx(elementos*x_a+(1-elementos)*xb)
    return plt.plot(x, res, color="blue", label="f(Lambda*x_a+(1-Lambda)*x_b)", linewidth=3)


x_a = float(input("ingresa el valor de x_a: "))
x_b = float(input("ingresa el valor de x_b: "))
lamda = float(input("ingresa el valor de lamda: "))

comprobar(x_a, x_b, lamda)

# graficarrecta
# graficar graficar_fx
# izq

plt.legend(loc="lower left")
plt.grid(True)
plt.xlabel("X")
plt.ylabel("f(x)")
plt.show()
