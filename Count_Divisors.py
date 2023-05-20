a,b,n=map(int,input().split())
c=0
for i in range(a,b+1):
    if(i%n==0):
        c+=1
print(c)