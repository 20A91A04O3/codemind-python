a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=set(l1)
l4=set(l2)
c=0
c1=0
for i in l3:
    if i not in l2:
        c+=1
for i in l4:
    if i not in l1:
        c1+=1
print(c1+c)
