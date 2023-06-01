n=input()
for i in n:
    if(n.count(i)==2):
        print("Not Unique Number")
        break
else:
    print("Unique Number")