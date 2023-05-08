import re
import numpy as np

from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr
from sympy import lambdify


# =========================== RECONOCER PATRONES ===========================================
terminos = "\-{0,1}\+{0,1}\s{0,}\d{1,}\.{0,1}\d{0,}[a-zA-Z]{1,}\d{1}" # 4x1, -2x2, ..., xn
variables = "[a-zA-Z]{1,}\d{1}" # x1, x2, ..., xn
theta = "([0-9]{1,}\.{0,1}\d{0,}\s{0,}\*{0,1}\({1})" # 0, 0.0001, 0.000006

def fuerza_bruta(theta, x_1, x_2, delta_x):
    data = []
    for x_1 in np.arange(x_1, 5.0 + delta_x, delta_x):
        for x_2 in np.arange(x_2, 5.0 + delta_x, delta_x):
            if x_1 + x_2 <= 5:
                f_x = f(x_1, x_2)
                data.append((x_1, x_2, f_x))
    return data

if __name__ == "__main__":
    funcion_no_lineal = input("Ingrese la función de dos variables a trabajar: ")

    # =========================== COMPILAR EXPRESIONES REGULARES ==============================
    v = re.compile(variables)
    v = re.findall(v, funcion_no_lineal)
    theta = re.compile(theta)
    theta = re.search(theta, funcion_no_lineal)

    variables = list(set(v))

    theta = re.sub("\s{0,}\*{1}\({1}", "", theta.group())
    print(f"Theta => {theta}")

    # ============================ DEFINIR LA FUNCIÓN ==========================================
    symbols(variables)
    p = parse_expr(funcion_no_lineal, evaluate=False)
    f = lambdify(variables, p)

    theta = float(theta)
    delta_x = 0.0001

    x_1 = 0.0
    x_2 = 0.0

    data = fuerza_bruta(theta, x_1, x_2, delta_x)

    x = max(data)

    print(x)
