tuple = ([15, 7, 10], 'string', [15, 7, 10], 4, 8.0, 'item', 1035, 5,3, [5, 2, 3, 7])
lis = []
tuple = list(tuple)
print(tuple)
i = 0
for j in tuple:
    if type(tuple[i]) == type(lis):
        lis.append(tuple[i])  
    else:
        continue
    i += 1
    if i >= len(tuple)-1:
        break
print(lis)
