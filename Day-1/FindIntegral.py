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

import sympy as sp


def main():
    x = sp.symbols('x')

    form1 = x * sp.log(x)
    form2 = x ** 2
    form3 = sp.tan(sp.sin(x))

    intr1 = sp.integrate(form1, x)
    intr2 = sp.integrate(form2, x)
    intr3 = sp.integrate(form3, x)

    print("integration of ", form1, "is :: ", intr1)
    print("integration of ", form2, "is :: ", intr2)
    print("integration of ", form3, "is :: ", intr3)


if __name__ == "__main__":
    main()
