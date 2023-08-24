def prime(n:int)->int:
    if(n==1):
        return 0
    k=int(n*0.5+1)
    for i in range(2,k):
        if(n%i==0):
            return 0
    return 1
a=int(input())
def pal(a:str)->int:
    if(a[::-1]==a):
        return 1
    else:
        return 0
a=a+1
while(a):
    if(pal(str(a))==1 and prime(a)==1):
        print(a)
        break
    else:
        a+=1