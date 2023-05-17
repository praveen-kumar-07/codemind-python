n=int(input())
k=-1
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    k=k+2
    p=k
    while(p>0):
        p-=1
        print(i,end="")
    print()