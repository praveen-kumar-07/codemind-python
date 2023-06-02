n=int(input())
ls=list(map(int,input().split()))
s=''
for i in ls:
    s+=str(i)
s=int(s)+1
s=str(s)
for i in s:
    print(i,end=' ')