n=int(input())
ls=list(map(int,input().split()))
c=0
s=0
for i in ls:
    if(ls.count(i)>=int(n/2)):
        if ls.count(i)>s:
            s=ls.count(i)
            m=i
print(m)