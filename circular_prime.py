def isprime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
                break
        else:
            return True
    else:
        return False
a=int(input())
s=str(a)
s1=int(s[::-1])
if (isprime(a)==True) and (isprime(s1)==True):
    print("circular prime")
elif (isprime(a)==True) or (isprime(s1)==True):
    print("prime but not a circular prime")
else:
    print("not prime")