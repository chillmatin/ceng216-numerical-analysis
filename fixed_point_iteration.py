# Author: Matin Huseynzade
# Class: CENG216 - Numerical Analysis
# This code demonstrates the attaining of the fixed point value of cos(x) function by means of fixed point iteration



from math import *

x = float(input("cos(x) => x = "))
last = None

for i in range(1000):
    print(cos(x))
    x = cos(x)
    if last != x:
        last = x
    else:
        r = last
        break


print("cos(x) function converges to " + str(r))