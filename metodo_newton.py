from numpy import *
from sympy import *
import sys

from sympy.core import symbol

#variables simbolicas
x,y= symbol("x,y")

# se recibe la funcion
funcion = eval(input("Ingrese la funcion a evaluar: "))

t=0.9
epsilon=sys.float_info.epsilon

xn=0

#calculo de la hessiana inversa
primera_derivada_funcion=sympy.diff(funcion,x)
segunda_derivada_funcion=sympy.diff(primera_derivada_funcion,x)
hessiana=eval(str(segunda_derivada_funcion))
matriz_hessiana=Matrix([[hessiana]])
hessiana_inversa=matriz_hessiana.inv()

#calculo del gradiente
gradiente=eval(str(primera_derivada_funcion))


xn1=xn - t*hessiana_inversa[0]*gradiente

#incompleto