def isprime(s):
    if s>1:
        for i in range(2,s):
            if s%i==0:
                return False
                break
        else:
            return True
    else:
        return False
n=int(input())
l=[]
for i in range(1,n):
    if n%i==0 and isprime(i)==True:
        l.append(i)
if len(l)!=0:
    print(*l)
else:
    print(-1)
