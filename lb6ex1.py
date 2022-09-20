import math
a = int(input("введіть a:"))
b = int(input('введіть b:'))
h = int(input('введіть h:'))

for x1 in range(a,b,h):
    def f(x):
        y=float((math.cos(x))/(1+math.fabs(math.sin(x))))
        return y
        
    print(f(x1))