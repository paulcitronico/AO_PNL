%Autor Jean Pacheco

%limpiamos los valores
clc; clear all
%creamos la variable simbolica
syms x
%recibimos los parametros
fun=input('ingrese la funcion:');
valor_x=input('ingrese el valor de x:');
valor_deltax=input('ingrese el valor de deltax:');
% inline metodo para evaluar 
FUN=inline(fun,'x');
fun_evaluada=(FUN(valor_x+valor_deltax)-FUN(valor_x))/valor_deltax;
disp('la derivada evaluada es: ')
disp(fun_evaluada);