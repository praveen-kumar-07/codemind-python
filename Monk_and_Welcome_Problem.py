n=int(input())
ls1=list(map(int,input().split()))
ls2=list(map(int,input().split()))
for i in range(0,n):
    print(ls1[i]+ls2[i],end=" ")