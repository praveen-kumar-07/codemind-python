n=int(input())
ls=list(map(int,input().split()))
e,o=0,0
for i in ls:
    if(i%2==0):
        e+=i
    else:
        o+=i
print(abs(e-o))