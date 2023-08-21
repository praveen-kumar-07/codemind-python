n=input()
ls=[i for i in n]
c=0
for i in ls:
    if(ls.count(i)>1):
        print("Not Unique Number")
        c=1
        break
if c==0:
    print("Unique Number")