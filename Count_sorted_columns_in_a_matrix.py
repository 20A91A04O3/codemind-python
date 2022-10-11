m,n=map(int,input().split())
a=[[0]*n]*m
for i in range(m):
    a[i]=list(map(int,input().split()))
l=[]
for i in range(n):
    l1=[]
    for j in range(m):
        l1.append(a[j][i])
    l.append(l1)
c=0
for i in l:
    y=sorted(i)
    z=y[::-1]
    if i==y or i==z:
        c=c+1
print(c)