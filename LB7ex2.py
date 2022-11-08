s1 = input('Введіть перший рядок: ')
s2 = input('Введіть другий рядок: ')
s3 = input('Введіть третій рядок: ')
s1 = s1.split(' ')
s2 = s2.split(' ')
s3 = s3.split(' ')
s1_ix = 0
s2_ix = 0
s3_ix = 0
common =[]
for i in range(10000):
    if s1[s1_ix]==s2[s2_ix]:
        for j in range(10000):
            if s1[s1_ix]==s3[s3_ix]==s2[s2_ix]:
                common.append(s1[s1_ix])
                s3_ix = 0
                break
            else:
                s3_ix+=1
                if s3_ix >= len(s3):
                    s3_ix = 0
                    break
                    #чи всі 3 речення мають одинакові слова
        s2_ix=0
        s1_ix+=1
        if s1_ix >= len(s1):
            break
    else:
        s2_ix+=1
        if s2_ix >= len(s2):
            s2_ix=0
            s1_ix+=1
            if s1_ix >= len(s1):
                break
#нижче виведення шуканих слів
if len(common)>0:
    print('спільні слова:')
    for i in common:
        print(i)
else:
    print('не має спілььних слів')