import math
a = float(input("введіть a:"))
b = float(input('введіть b:'))
h = float(input('введіть h:'))
x=a
li=[]
for i in range (100):
        y=(math.cos(x))/(1+math.fabs(math.sin(x)))
        y = round(y,4)
        li.append(y)
        x+=h
        x=round(x,2)
        if x>b:
            break
for i in li:
        print(i)
lis=li
lis.sort()
lis.pop(0)
lis.pop(-1)
print (lis)