a=int(input())
b=int(input())
s=0
k=0
for i in range(1,a):
    if(a%i==0):
        s+=i
for i in range(1,b):
    if(b%i==0):
        k+=i
if(a==k):
    print("Amicable")
else:
    print("Not Amicable")