def prime(n):
    k=int(n**0.5+1)
    for i in range(2,k):
        if(n%i==0):
            return False
    return True
n=input()
if(prime(int(n))):
    if(prime(int(n[::-1]))):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
    
    