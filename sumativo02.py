# importamos las librerias
import numpy as np
import matplotlib.pyplot as plt
import math


# predefinimos una funcion a evaluar
def f_x(x):
    res1 = pow(x, 3)
    res2 = pow(x, 2)
    res3 = res1-res2  # + math.sin(x)
    return res3


# creamos la funcion para evaluar su estado
# concavo, convexo o indeterminable
def evaluar_funcion(x_a, x_b, lmda):
    resrelativa = ""
    respuestafinal = ""
    for i in np.arange(0, 1, lmda):
        izq = f_x(i*x_a+(1-i)*x_b)
        der = i*f_x(x_a)+(1-i)*f_x(x_b)
        if(izq < der):
            respuestafinal = "convexa"
            if(resrelativa == "concava"):
                respuestafinal = "indeterminada"
            if(resrelativa == "indeterminada"):
                respuestafinal = "indeterminada"
        if(izq > der):
            respuestafinal = "concava"
            if(resrelativa == "convexa"):
                respuestafinal = "indeterminada"
            if(resrelativa == "indeterminada"):
                respuestafinal = "indeterminada"

        resrelativa = respuestafinal
    return print(respuestafinal)


# se genera la grafica de la funcion
def grafica(x_a, x_b):
    arrayx = []
    arrayy = []
    # llenamos el arreglo de x
    for i in np.arange(x_a, x_b, 0.1):
        arrayx.append(i)
    # llenamos el arreglo de y
    for i in arrayx:
        arrayy.append(f_x(i))

    # ploteamos el grafico
    plt.plot(arrayx, arrayy, color='black')


# se solicitan los datos
# cabe señalar que se debe hacer un casting
x_a = float(input("ingresar valor de x_a: "))
x_b = float(input("ingresar valor de x_b: "))
lmda = float(input("ingresar valor de lambda: "))


# hacemos el llamado a las funciones
evaluar_funcion(x_a, x_b, lmda)
grafica(x_a, x_b)

plt.show()
