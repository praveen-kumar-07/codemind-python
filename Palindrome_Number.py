t=int(input())
for i in range(0,t):
    n=input()
    s=n[::-1]
    if(int(n)==int(s)):
        print("True")
    else:
        print("False")