def isprime(a):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                return False
        else:
            return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if (isprime(i)==True):
        c+=1
print(c)