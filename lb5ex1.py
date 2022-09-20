import math
x = float(input('Введіть x: '))
def func (x):
    if x > 12.1:
       return math.log(abs(x-1), math.e)+ math.log10(abs(x**0.7*x+2))
    if x >=-5.7 and x <= 12.1:
        return math.e*4*x**7+2 - x**1/3
    else:
        return 4.27*x+4.33*x**2+math.sin(x+1)
print (func(x))