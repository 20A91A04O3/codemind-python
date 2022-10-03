l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=0
d=0
for i in range(len(l1)):
    if l1[i]>l2[i]:
        c+=1
    elif l2[i]>l1[i]:
        d+=1
print(c,d)