n=input()
while(len(n)!=1):
    s=0
    for i in n:
        s+=int(i)**2
    n=str(s)
if(n=='1' or n=='7'):
    print("True")
else:
    print("False")