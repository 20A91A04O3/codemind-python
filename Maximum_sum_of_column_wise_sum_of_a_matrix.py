r,c=map(int,input().split())
l1=[]
for i in range(r):
    l=list(map(int,input().split()))
    l1.append(l)
l3=[]
for i in range(len(l1[0])):
    s=0
    for j in range(len(l1)):
        s+=l1[j][i]
    l3.append(s)
print(max(l3))