n=int(input())
ls=list(map(int,input().split()))
c=0
for i in range(0,n):
    if(ls[i]==0):
        print("0",end=" ")
        c+=1
for i in range(0,n-c):
    print("1",end=" ")