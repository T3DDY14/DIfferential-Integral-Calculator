from sympy import *
from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)
print(diff(cos(x), x))
print(diff(exp(x**2), x))
eq = input("equation")
print(diff(exp(eq),x))