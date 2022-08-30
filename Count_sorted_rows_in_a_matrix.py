a,m=map(int,input().split())
m1=[]
for i in range(a):
    l=list(map(int,input().split()))
    m1.append(l)
c=0
for i in m1:
    l1=sorted(i)
    l2=l1[::-1]
    if i==l1 or i==l2:
        c+=1
print(c)