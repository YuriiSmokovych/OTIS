import math
a = float(input("введіть a:"))
b = float(input('введіть b:'))
h = float(input('введіть h:'))
c=a
while c<=b:
    def f(x):
        y =(math.cos(x))/(1+math.fabs(math.sin(x)))
        return y
    print (f(c))
    c+=h

