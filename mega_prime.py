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
n=int(input())
if isprime(n)==True:
    s=str(n)
    c=0
    for i in s:
        if isprime(int(i))==True:
            c+=1
    if c==len(s):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
