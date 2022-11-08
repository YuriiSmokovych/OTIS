from array import*
mynum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
masiv = array('i',mynum)
for i in range(len(masiv)):
    if i %2 == 0:
        masiv[i]=10**i
    else:
        continue
print(masiv)
print(masiv[1:-1])