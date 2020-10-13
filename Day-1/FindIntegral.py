# -*- coding: utf-8 -*-
"""
Python Codes to find Integrals of the following function :
1.) xlog(x)
2.) x^2
3.) tan(sin(x))

Created on Tue Oct 13 10:08:37 2020
@author: Gyan Krishna

install the following packages:-
pip install sympy
"""

from sympy import *


def main():
    x = symbols('x')

    form1 = x * log(x)
    form2 = x ** 2
    form3 = tan(sin(x))

    intr1 = integrate(form1, x)
    intr2 = integrate(form2, x)
    intr3 = integrate(form3, x)

    print("intrgration of ", form1, "is :: ", intr1)
    print("intrgration of ", form2, "is :: ", intr2)
    print("intrgration of ", form3, "is :: ", intr3)


if __name__ == "__main__":
    main()

