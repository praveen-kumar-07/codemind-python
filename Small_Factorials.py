t=int(input())
for i in range(0,t):
    n=int(input())
    s=1
    while n!=1:
        s=s*n
        n-=1
    print(s)