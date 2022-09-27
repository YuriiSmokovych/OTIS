import math
a = float(input("введіть a:"))
b = float(input('введіть b:'))
h = float(input('введіть h:'))
x=a
y=0.0
for i in range(100):
    y =(math.cos(x))/(1+math.fabs(math.sin(x)))
    y = round(y,4)
    print(i,"\t",x,"\t",y)
    x+=h
    x=round(x,2)
    if x>b:
        break