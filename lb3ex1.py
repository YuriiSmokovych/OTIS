import sys 
a=int(sys.argv[1])
a1=a//1000
a2=a//100%10
a3=a//10%10
a4 =a%10
reply1 =a1*10 +a2
reply2 =a3*10 +a4
print (reply1)
print (reply2)