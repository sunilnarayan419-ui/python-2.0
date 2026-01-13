# Module = a file containing code you want to include in your program 
# use ' Import' to include a module (build in or your own)
# useful to break up a large program reusable separate files

print(help("modules"))
import math
import math as m 
from math import pi 

print(pi)
a , b ,c ,d = 1, 2, 3, 4
print(pi**c)    

# Ex 

x = pi

def sqr(x):
    return x **2
def cube(x):
    return x **3
def circumfrence(radius):
    return 2 * pi * radius 

def area(radius):
    return pi* radius 