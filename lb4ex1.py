import math
x=float(input("Введіть х")) 
def func1(x):
    y = math.cos(x) + math.log(abs(x)+1)
    z = math.exp(0.7*x) + math.pow(4, 3.3*x+1)
    c = math.pow (0.9*x, math.sqrt(2*x))
    return ((y/z) - c)
print (func1(x))