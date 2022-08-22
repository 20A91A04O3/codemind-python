a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l5=[]
for i in l1:
    if i not in l2:
        l5.append(i)
for i in l2:
    if i not in l1:
        l5.append(i)
print(*l5)