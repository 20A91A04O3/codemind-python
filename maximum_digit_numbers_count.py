n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    s=str(abs(i))
    l1.append(len(s))
for i in range(len(l1)):
    if max(l1)==l1[i]:
        if l[i] not in l2:
            l2.append(l[i])
print(*l2)