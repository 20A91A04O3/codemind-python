t=int(input())
l1=[]
l2=[]
for i in range(1,(t*2)+1):
    n=int(input())
    if i<=(t):
        l1.append(n)
    else:
        l2.append(n)
c=0
l1=list(sorted(l1))
l2=list(sorted(l2))
for i in range(t):
    if l2[i]<l1[i]:
        c+=1
print(c)