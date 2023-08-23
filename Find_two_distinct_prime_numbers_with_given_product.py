def prime(n:int)->int:
    if(n==1):
        return 0
    k=int(n**0.5+1)
    for i in range(2,k):
        if(n%i==0):
            return 0
    return 1
n=int(input())
c=0
for i in range(0,n//2):
    for j in range(0,n):
        if(prime(i) and prime(j) and i*j==n):
            print(i,j)
            c=1
            break
    if(c==1):
        break
else:
    print(-1)