
n=int(input())
for i in range(1,n+1):
    k=n+1
    for j in range(1,n+1):
        k-=1
        print("%d"%(k),end=" ")
    print()
