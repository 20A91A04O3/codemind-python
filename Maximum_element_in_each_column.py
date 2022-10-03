r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
m1=[]
for i in range(c):
    l=[]
    for j in range(r):
        l.append(m[j][i])
    m1.append(l)
for i in m1:
    print(max(i))