
# coding: utf-8

# In[7]:


import math 
from sympy import *
x=symbols('x')

def factorial(n):
    M=1
    F=1
    while M<float(n):
        M=M+1
        F=F*M
    return (F)
    
n=input('da el grado de la derivada')
r=input('dame un numero x')

fun=(x**2-1)**float(n)
derivada=diff(fun,x,n)
xevaluado=derivada.subs(x,float(r))

polinomio=(1/(2**float(n)*factorial(n)))*derivada

derivada2=diff(polinomio,x,1)

print("El facotial de n es: ", factorial(n))
print("La derivada de la funcion es: ", derivada)
print("Valor de la derivada es: ", xevaluado)
print("El polinomio es: ", polinomio)
print("La derivada del polinomio es: ", derivada2)

