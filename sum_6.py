# librerias
import numpy as np
from sympy import *

# segundas derivadas respeco a x1 y x2


def diff_primera_derivada_x1(x12, x22, delta_x):
    sol = primera_derivada_x1.subs([(x1, (x12+delta_x)), (x2, x22)]) - \
        primera_derivada_x1.subs([(x1, x12), (x2, x22)])/delta_x
    return sol


def diff_primera_derivada_x2(val1, val2, delta_x):
    sol = primera_derivada_x2.subs([(x2, (x22+delta_x)), (x1, x12)]) - \
        primera_derivada_x2.subs([(x2, x22), (x1, x12)])/delta_x
    return sol


def diff_de_x1x2(x12, x22, delta_x):
    sol = primera_derivada_x1.subs([(x2, (x22+delta_x)), (x1, x12)]) - \
        primera_derivada_x1.subs([(x2, x22), (x1, x12)])/delta_x
    return sol


# variables simbolicas
x1, x2 = symbols("x1,x2")

# se recibe la funcion
funcion = eval(input("Ingrese la funcion a evaluar: "))

# se realiza la primera derivada
primera_derivada_x1 = diff(funcion, x1)
primera_derivada_x2 = diff(funcion, x2)

# se obtiene la solucion al sistema de ecuanciones
solucion_SE = solve((primera_derivada_x1, primera_derivada_x2), (x1, x2))

# se muestra la solucion
print("la solucion al sistema de ecuanciones es: ", solucion_SE)

# se piden los valores de los puntos y el delta x
x12 = float(eval(input("ingrese el valor del x1: ")))
x22 = float(eval(input("ingrese el valor del x2: ")))
delta_x = float(eval(input("ingrese el valor de delta x: ")))

# se resuelve H(x)
H_x = (diff_primera_derivada_x1(x12, x22, delta_x)*diff_primera_derivada_x2(x12, x22, delta_x)
       )-(diff_de_x1x2(x12, x22, delta_x)**2)

# desicion logica
if H_x < 0:
    print(H_x, " es punto silla")
elif H_x > 0 and diff_primera_derivada_x1(x12, x22, delta_x) < 0:
    print(H_x, " es maximo local")
elif H_x > 0 and diff_primera_derivada_x1(x12, x22, delta_x) > 0:
    print(H_x, " es minimo local")
elif H_x == 0:
    print(H_x, " falta informacion")
