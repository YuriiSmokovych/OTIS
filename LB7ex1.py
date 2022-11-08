s1 = input('Введіть рядок: ')
i=0
end=0
while s1[i].isdigit()==False:
    i+=1
while s1[end].isdigit()==False:
    end-=1
print(s1[:i+1]+s1[end:])