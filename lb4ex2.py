import math
x=float(input("Введіть х"))
y=float(input("Введіть y")) 
z=float(input("Введіть z")) 
def func1 (x):
    a = math.pow(0.7*math.cos(x) + math.log(abs(y)), 1/5) + math.pow(math.e, z+x)
    return (a)
print (func1(x))