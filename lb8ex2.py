import numpy as np
import random
N = int(input('введіть розмір матриці: '))
masiv1 = np.zeros((N,N))
for i in range(N):
    for j in range (N):
        masiv1[i, j] = random.randint(1,35)
masiv1 = np.array(masiv1,dtype=np.int64)
print(masiv1)
#створення матриці та перетворення її на тип даних int64
suma1 = 0
suma2 = 0
for i in range(N):
    for j in range (N):
        if i < j:
            suma1 += masiv1[i, j]
        elif i > j:
            suma2 += masiv1[i, j]
print('сума вище:',suma1,'\nсума нижче:',suma2)
