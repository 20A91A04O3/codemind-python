n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
for i in l:
    s=(str(abs(i)))
    l1.append(len(s))
c=0
for i in l1:
    if i==k:
        c+=1
print(c)