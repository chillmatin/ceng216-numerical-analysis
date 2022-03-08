# Author: Matin Huseynzade
# Date: 08-03-2022
# Description: This program uses the bisection method to find the root of a function
# Class: CENG216

def f(x):

    return eval(function)

from math import *


function = input("f(x) = ")
print("Input interval [x1, x2]")
a = float(input("x1 = "))
b = float(input("x2 = "))
steps = int(input("Bisection steps: "))


c = 0

print("steps, x0, f(x0), mid, f(mid), x1, f(x1)")
for i in range(steps):
    print("(", end="")
    print( i, a, f(a), c, f(c), b, f(b), sep=", ", end="")
    print(")", end="")
    print()


    c = (a + b) / 2
    if f(c) == 0:
        break
    
    elif f(a)*f(c) < 0:
        b = c
    else:
        a = c
    
    
print("Root interval [", a, ", ", b, "]")
print("Root = ", (a+b)/2)
