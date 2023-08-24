def prime(n:int)->int:
    if(n==1):
        return 0
    k=int(n**0.5+1)
    for i in range(2,k):
        if(n%i==0):
            return 0
    return 1
def next_prime(n):
    if(prime(n)==1):
        return n
    else:
        return next_prime(n+1)
a=int(input())
b=int(input())
n=next_prime(a+b+1)
print(n-a-b)
    