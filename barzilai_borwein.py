from sympy import *

# variables simbolicas
x1, x2 = symbols("x1,x2")

eta=0.0006
t=0.1

# se recibe la funcion
funcion = eval(input("Ingrese la funcion a evaluar: "),{"x1":x1, "x2":x2})

#punto a evaluar
punto=input("Ingrese un punto a evaluar: ").split(",")

#se llena la matriz
matriz=Matrix([[float(punto[0])],[float(punto[1])]])


#calculo del gradiente
primera_derivada_x1=funcion.diff(x1)
primera_derivada_x2=funcion.diff(x2)
gradiente=Matrix([[primera_derivada_x1],[primera_derivada_x2]])

#calculo gradiente desendiente
print("los puntos son_: ")
while(float(gradiente.subs([(x1,matriz[0]),(x2,matriz[1])]).norm())>=eta):
    gradiente1=gradiente.subs([(x1,matriz[0]),(x2,matriz[1])])
    deltax= -t*gradiente1
    matriz=matriz+deltax
    gradiente2=gradiente.subs([(x1,matriz[0]),(x2,matriz[1])])
    denominador=gradiente2-gradiente1
    gradiente1=gradiente2
    t=deltax.dot(denominador)/denominador.dot(denominador)
    #punto solucion
    print(" ",matriz[0],",",matriz[1])