from sympy import *
from math import sqrt

# variales simbolicas
x, y = symbols("x,y")

# puntos a evaluar
# se crean las tuplas
# punto para Himmelblau's
puntoHb = Matrix([[float(-4)], [float(-4)]])
# punto para Booth
puntoBth = Matrix([[float(1)], [float(3)]])
# funciones a evaluar

# Himmelblau's
fun1 = str((x**2+y-11)**2+(x+y**2-7)**2)
# Booth
fun2 = str((x+2*y-7)**2+(2*x+y-5)**2)

# evaluamos las variables simbolicas en las funciones
fun1 = eval(fun1, {"x": x, "y": y})
fun2 = eval(fun2, {"x": x, "y": y})


# se recibe el valor de t y eta por teclado
t = float(input("ingrese un valor fijo para t: "))
eta = float(input("Ingrese un valor para eta: "))

# calculamos el gradiente de las funciones escogidas
# primera derivada Himmelblau's
primera_derivada_x_f1 = diff(fun1, x)
primera_derivada_y_f1 = diff(fun1, y)

# print(primera_derivada_x_f1)
# print(primera_derivada_y_f1)

# primera derivada Booth
primera_derivada_x_f2 = diff(fun2, x)
primera_derivada_y_f2 = diff(fun2, y)

# print(primera_derivada_x_f2)
# print(primera_derivada_y_f2)

# creamos el gradiente
gradiente_f1 = Matrix([[primera_derivada_x_f1], [primera_derivada_y_f1]])
gradiente_f2 = Matrix([[primera_derivada_x_f2], [primera_derivada_y_f2]])

# print(gradiente_f1)
# print(gradiente_f2)

# se evalua el gradiente en el punto
gra_punto_f1 = gradiente_f1.subs([(x, puntoHb[0]), (y, puntoHb[1])])
gra_punto_f2 = gradiente_f2.subs([(x, puntoBth[0]), (y, puntoBth[1])])
# print(gra_punto_f1)
# print(gra_punto_f2)

# generamos la norma
norma_gra_f1 = ((gra_punto_f1[0]**2+gra_punto_f1[1]**2))**(0.5)
norma_gra_f2 = ((gra_punto_f2[0]**2+gra_punto_f2[1]**2))**(0.5)
# print(norma_gra_f1)
# print(norma_gra_f2)

# generamos el bucle condicional
while(norma_gra_f1 >= eta):
    deltaxn = -gradiente_f1.subs([(x, puntoHb[0]), (y, puntoHb[1])])
    puntoHb = puntoHb+(t*deltaxn)
    # print(norma_gra_f1)
    gra_punto_f1 = gradiente_f1.subs([(x, puntoHb[0]), (y, puntoHb[1])])
    norma_gra_f1 = sqrt((gra_punto_f1[0]**2)+(gra_punto_f1[1]**2))
print("punto hb es: ", puntoHb)

while(norma_gra_f2 >= eta):
    deltaxn = -gradiente_f2.subs([(x, puntoBth[0]), (y, puntoBth[1])])
    puntoBth = puntoBth+(t*deltaxn)
    # print(puntoBth)
    gra_punto_f2 = gradiente_f2.subs([(x, puntoBth[0]), (y, puntoBth[1])])
    norma_gra_f2 = sqrt((gra_punto_f2[0]**2)+(gra_punto_f2[1]**2))
print("punto bth es: ", puntoBth)
