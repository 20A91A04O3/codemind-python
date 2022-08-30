a,b=map(int,input().split())
m1=[]
m2=[]
for i in range(a):
    l=list(map(int,input().split()))
    m1.append(l)
l1=[]
for i in m1:
    l1.append(sum(i))
print(max(l1))
    