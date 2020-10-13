# Run the command below if package not installed
# pip install sympy

# Importing sympy
from sympy import *

init_printing(use_unicode=True)

x = Symbol('x')

# Expressions
exp1 = x * log(x)
exp2 = x ** 2
exp3 = tan(sin(x))

print("Integration of", exp1, "is", integrate(exp1, x))
print("Integration of", exp2, "is", integrate(exp2, x))
print("Integration of", exp3, "is", integrate(exp3, x))
