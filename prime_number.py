def prime(n:int)->int:
    k=int(n**0.5+1)
    for i in range(2,k):
        if(n%i==0):
            return 0
    return 1
n=int(input())
if(prime(n)):
    print("prime")
else:
    print("not a prime")