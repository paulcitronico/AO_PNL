import sympy
import numpy as np

#funciones
def getfuncionx(funcion,x,y):
    variablex=eval(funcion)
    return variablex

def getfunciony(funcion,x,y):
    variabley=eval(funcion)
    return variabley

def derivada(x,deltax,y,deltay):
    resp1x=getfuncionx(str(funcion),x+deltax,y)
    resp2x=getfuncionx(str(funcion),x,y)
    respfx=(resp1x-resp2x)/deltax
    resp1y=getfunciony(str(funcion),x,y+deltay)
    resp2y=getfunciony(str(funcion),x,y)
    respfy=(resp1y-resp2y)/deltay
    return (respfx,respfy)

#inicializacion de variables
funcion="x**2 + y**2"
x = [2,3,4,5,6]
deltax = [0.02,0.04, 0.06, 0.08, 0.10]
y = [1,3,5,6,7]
deltay = [0.01, 0.5, 0.07, 0.09, 0.11]

for i in range(len(x)):
    print(derivada(x[i],deltax[i],y[i],deltay[i]))