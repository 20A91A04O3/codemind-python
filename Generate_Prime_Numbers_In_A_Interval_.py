from math import *
def isprime(s):
    if s>1:
        for i in range(2,int(sqrt(s))+1):
            if s%i==0:
                return False
                break
        else:
            return True
    else:
        return False
    

a=int(input())
b=int(input())
for i in range(a,b+1):
    if isprime(i):
        print(i)
