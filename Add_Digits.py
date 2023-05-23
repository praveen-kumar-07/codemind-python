n=(input())
while(len(n)!=1):
    s=0
    for i in n:
        s=int(i)+int(s)
    n=str(s)
print(int(n))
        