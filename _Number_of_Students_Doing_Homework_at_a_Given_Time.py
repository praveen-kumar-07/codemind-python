nst=int(input())
st=list(map(int,input().split()))
nen=int(input())
en=list(map(int,input().split()))
t=int(input())
c=0
for i in range(0,nst):
    for j in range(st[i],en[i]+1):
        if(j==t):
            c+=1
            break
print(c)