import re
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr
from sympy import lambdify
import numpy as np

def func_obj(x_1, x_2, theta):
    return 1.20*x_1+1.16*x_2-theta*(2*x_1**2+x_2**2+(x_1+x_2)**2)

# =========================== RECONOCER PATRONES ===========================================
terminos = "\-{0,1}\+{0,1}\s{0,}\d{1,}\.{0,1}\d{0,}[a-zA-Z]{1,}\d{1}" # 4x1, -2x2, ..., xn
variables = "[a-zA-Z]{1,}\d{1}" # x1, x2, ..., xn
theta = "([0-9]{1,}\.{0,1}\d{0,}\s{0,}\*{0,1}\({1})" # 0, 0.0001, 0.000006
digit = "[0-9]{1,}" # 1, 12, 1.2, 120, etc

def fuerza_bruta(theta:float, max_range, x1, x2, delta_x):
    if theta == 0.0:
        print("El problema tiene solución a través de programación lineal.")
        maximiza = False 
        x = 0
    else:
        data = []
        f_o = []
        for x_1 in np.arange(x1, max_range, delta_x):
            for x_2 in np.arange(x2, max_range, delta_x):
                if x_1 + x_2 <= max_range:
                    f_x = func_obj(x_1, x_2, theta)
                    f_o.append(f_x)
                    data.append((x_1, x_2, f_x))
        x = max(f_o)
        index = f_o.index(x)
        maximiza = (data[index][0], data[index][1])
    return maximiza, x
    
if __name__ == "__main__":
    funcion_no_lineal = input("Ingrese la función de dos variables a trabajar: ")

    # =========================== COMPILAR EXPRESIONES REGULARES ==============================
    v = re.compile(variables)
    v = re.findall(v, funcion_no_lineal)
    theta = re.compile(theta)
    theta = re.search(theta, funcion_no_lineal)
    digit = re.compile(digit)

    # ============================ OBTENER PARTES DE LA FUNCIÓN ===============================
    variables = list(set(v))
    if len(variables) == 2:
        theta = re.sub("\s{0,}\*{1}\({1}", "", theta.group())
        print(f"Theta => {theta}")

        # ============================ DEFINIR LA FUNCIÓN ==========================================
        s = symbols(variables)
        p = parse_expr(funcion_no_lineal, evaluate=False)
        f = lambdify(variables, p)

        min_range = 0
        max_range = 5

        x1 = min_range
        x2 = min_range

        delta_x = 0.0001

        maximiza, x = fuerza_bruta(float(theta),max_range,x1, x2, delta_x)

        print(f"Maximiza: {maximiza}, Valor: {x}")
    else:
        print("Nuestro programa solo debe reconocer 2 variables dentro de la función objetivo")