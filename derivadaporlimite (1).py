# Autor: Jean Paul Pacheco


# funciones
def getfuncion(fun, x):
    variable = eval(fun)
    return variable


# Lectura de datos
fun = input("ingrese una funcion: ")
x = float(input("ingrese x: "))
deltax = float(input("delta x: "))

# calculo de la derivada
resp1 = float(getfuncion(fun, x+deltax))
resp2 = float(getfuncion(fun, x))
respf = (resp1-resp2)/deltax

# mostrar los datos
print("la derivada es: ")
print(respf)
