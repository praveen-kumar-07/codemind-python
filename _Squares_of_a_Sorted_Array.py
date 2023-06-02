def square(n):
    return n*n
n=int(input())
ls=list(map(int,input().split()))
lst=[square(i) for i in ls]
lst.sort()
for i in lst:
    print(i,end=" ")