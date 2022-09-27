import math
a = float(input("введіть a:"))
b = float(input('введіть b:'))
h = float(input('введіть h:'))
x=a
while x<=b:
    y =(math.cos(x))/(1+math.fabs(math.sin(x)))
    y=round(y,4)
    print(x,"\t",y)
    x+=h
    x=round(x,2)




