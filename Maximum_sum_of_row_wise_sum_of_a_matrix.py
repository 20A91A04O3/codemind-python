r,c=map(int,input().split())
l1=[]
for i in range(r):
    l=list(map(int,input().split()))
    l1.append(l)
l3=[]
for i in l1:
    l3.append(sum(i))
print(max(l3))
    