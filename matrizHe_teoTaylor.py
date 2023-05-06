import sympy
from sympy import *
import matplotlib.pyplot as plt

#Metodos a utilizar
def derivada(func,x):
    func_derivada=diff(func,x)
    return func_derivada

def evaluar(fc,x):
    y=eval(fc)
    return y

def graficar(inteX,inteY,inteT):
    plt.plot(inteX,inteY,'r-', label='Funcion Original(Exacta)')
    plt.plot(inteX,inteT,'b:', label="funcion con estimacion Taylor")
    plt.title("grafica")
    plt.xlabel("X")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

#inicializacion de variables
x=var('x')
delta=0.01
t=1

#recibimos los datos
print("Ingrese funcion a evaluar: ")
fc=raw_input("funcion: ")
xa=float(input("ingrese valor de xa: "))
xb= float(input("ingrese vaor de xb: "))

#creamos el intervalo
inter_x=np.arange(xa,xb,delta)
inter_y=[]
inter_T=[]

#derivamos
primeraDerivada=derivada(fc,x)
segundaDerivada=derivada(primeraDerivada,x)

#creamos el intervalo de y

for z in inter_x:
    z=z+delta
    y=evaluar(str(fc),z)
    inter_y.append(y)

#creamos el intervalo por teorema taylor
for i in inter_x:
    Taylor=evaluar(fc,i)+evaluar(str(primeraDerivada),i)*delta+0.5*delta*(evaluar(str(segundaDerivada),i+t*delta))*delta
    inter_T.append(Taylor)

graficar(inter_x,inter_y,inter_T)