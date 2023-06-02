n=int(input())
m=int(input())
ls=[]
for i in range(0,n):
    lst=list(map(int,input().split()))
    ls.append(lst)
s=0
for i in ls:
    s=s+sum(i)
print(s)