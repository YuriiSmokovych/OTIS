import math
x1=float(input("Введіть х"))
y1=float(input("Введіть y")) 
z1=float(input("Введіть z")) 
def func1 (x, y, z):
    a = math.pow(0.7*math.cos(x) + math.log(abs(y)), 1/5) + math.pow(math.e, z+x)
    return (a)
f= func1(x1,y1,z1)
print (f)
