n=int(input())
h=0
s=0
for i in range(1,n+1):
    h+=(i*i)
    s+=i
v=(s*s)-h
print(v)