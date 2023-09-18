n=int(input())
ls=list(map(int,input().split()))
c=0
for i in range(0,len(ls)-2):
    if(ls[i]%2==0 and ls[i+2]%2==1 or ls[i]%2==1 and ls[i+2]%2==0):
        c+=1
print(c)