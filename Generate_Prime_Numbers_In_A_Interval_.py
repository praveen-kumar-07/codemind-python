def prime(n:int)->int:
    k=int(n**0.5+1)
    if(n==1):
        return 0
    for i in range(2,k):
        if(n%i==0):
            return 0
    return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(prime(i)):
        print(i)