# -*- coding: utf-8 -*-
"""
Python code to change temperatures :
From Celcius to Farenhite & ViceVersa
Input your temperature
and change itCreated on Tue Oct 13 09:45:41 2020
@author: Gyan Krishna
"""


def main():
    temp = input("enter the temperature")
    l = int(len(temp))
    postfix = temp[l - 1]

    if postfix == 'C' or postfix == 'c':

        celcius = int(temp[0:l - 1])
        farenheit = 9 / 5 * celcius + 32

        print("Temp in farenheit is :: ", farenheit)
    elif postfix == 'F' or postfix == 'f':

        farenheit = int(temp[0:l - 1])
        celcius = 5 / 9 * (farenheit - 32)

        print("Temp in Celcius is :: ", celcius)
    else:
        print("input format error!")


if __name__ == "__main__":
    main()
