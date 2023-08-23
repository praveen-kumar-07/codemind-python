def prime(n:int)->int:
    k=int(n**0.5+1)
    for i in range(2,k):
        if(n%i==0):
            return 0
    return 1
def prev_prime(n):
    while(n):
        if(prime(n)):
            break
        else:
            n-=1
    return n
def next_prime(n):
    while(n):
        if(prime(n)):
            break
        else:
            n+=1
    return n
n=int(input())
fn=prev_prime(n)
bn=next_prime(n)
if(n-fn>bn-n):
    print(bn-n)
else:
    print(n-fn)