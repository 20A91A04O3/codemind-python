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
l=[]
l1=[]
if isprime(n):
    print(0)
else:
    for i in range(1,n*2):
        if isprime(i) and i<n:
            l.append(i)
        elif isprime(i) and i>n:
            l1.append(i)
    if abs(l[-1]-n)<abs(n-l1[0]):
        print(abs(l[-1]-n))
    else:
        print(abs(l1[0]-n))
        
