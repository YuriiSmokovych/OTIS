a = float(input('Введіть висоту бруска : '))
b = float(input('Введіть ширину бруска: '))
c = float(input('Введіть довжину бруска: '))
m = float(input('Введіть висоту отвору: '))
n = float(input('Введіть ширину отвору: '))
am=()
bm=()
cm=()
an=()
bn=()
cn=()
if a<=m:
    am = a
#сторона бруска що проходить
if a<=n:
    an = a
if b<=m:
    bm = b
if b<=n:
    bn = b
if c<=m:
    cm = c
if c<=n:
    cn = c
#перевірка чи сторони менші за висоту 'am' або ширину 'an' отвору
if (am and bn) or (an and bm) or (am and cn) or (an and cm) or (cm and bn) or (cn and bm):
# якщо висота бруска і ширина проходять в різна отвори, задача виконана
# і так до інших 'and' та 'or'
    print("брусок проходить в отвір")
else:
    print ('not')
