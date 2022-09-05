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
l1=[]
for i in l:
    for j in l:
        if (i*j==n) and (i not in l1) and (j not in l1):
            l1.append(i)
            l1.append(j)
            
if len(l1)!=0:
    print(*l1[0:3])
else:
    print(-1)