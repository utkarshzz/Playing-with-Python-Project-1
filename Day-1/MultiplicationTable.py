# -*- coding: utf-8 -*-
"""
Python Code that prints only 10 multiples of any number.
Created on Tue Oct 13 10:03:21 2020
@author: Gyan Krishna
"""
def main():
    num = int(input("enter a number! "))
    for i in range(1,1+10):
        print(i," * ",num," = ",num*i)

if __name__ == "__main__":
    main()