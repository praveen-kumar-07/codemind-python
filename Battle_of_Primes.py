def prime(n):
    k=int(n**0.5+1)
    if(n==1):
        return False
    for i in range(2,k):
        if(n%i==0):
            return False
    return True
def next_prime(n):
    while(n):
        if(prime(n)):
            return n
        n+=1
a=int(input())
b=int(input())
c=next_prime(a+b+1)
print(c-a-b)
            