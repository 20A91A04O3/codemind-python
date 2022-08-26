n=input()
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
l3=[]
l4=[]
if len(l1)<len(l2):
    for i in range(len(l1)):
        l3.append(l2[i])
        l3.append(l1[i])
    else:
        for i in range(len(l1),len(l2)):
            l3.append(l2[i])
else:
    for i in range(len(l2)):
        l4.append(l2[i])
        l4.append(l1[i])
    else:
        for i in range(len(l2),len(l1)):
            l4.append(l1[i])
if len(l3)!=0:
    if len(l3)%2:
        l3.append(0)
        print(*l3)
    else:
        print(*l3)
if len(l4)!=0:
    if len(l4)%2:
        l4.append(0)
        print(*l4)
    else:
        print(*l4)
