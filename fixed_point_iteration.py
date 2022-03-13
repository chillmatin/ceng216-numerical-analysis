# Author: Matin Huseynzade
# Class: CENG216 - Numerical Analysis
# This code demonstrates the attaining of the fixed point value of cos(x) function by means of fixed point iteration
# Geometric view of the Fixed Point Iteration is also plotted out


from math import *
import matplotlib.pyplot as plt
import numpy as np

a = float(input("cos(a) => a = "))



last = None

x = np.linspace(-pi,pi,100)
y = x
plt.plot(x,y, label = "y=x", color="b")

#x_set = [a, a, cos(a),cos(a),cos(cos(a)), cos(cos(a))]
#y_set = [0,cos(a), cos(a),cos(cos(a)), cos(cos(a)),cos(cos(cos(a)))]

x_set = [a]
y_set = [-pi]
x_set.append(a)
y_set.append(a)

for i in range(1000):

    print(cos(a))

    
    x_set.append(cos(a))
    x_set.append(cos(a))
    y_set.append(a)
    a = cos(a)
    
    y_set.append(a)
      

    if last != a:
        last = a
    else:
        r = last
        break


plt.plot(x_set, y_set, color="r", linestyle=":")
plt.xlim(-pi, pi)
plt.show()

print("cos(x) function converges to " + str(r))
