from math import *
def isprime(i):
    if i>1:
        for j in range(2,int(sqrt(i))+1):
            if i%j==0:
                return False
                break
        else:
            return True
    else:
        return False
n=int(input())
l=[]
for i in range(1,n+1):
    if (n%i==0) :
        l.append(i)
c=0
for i in l:
    if isprime(i)==False:
        c+=1
print(c)
        
        