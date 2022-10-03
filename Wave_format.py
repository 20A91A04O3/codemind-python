n=int(input())
l=list(map(int,input().split()))
l2=[]
l3=[]
for i in range(len(l)):
    a=l.pop(l.index(max(l)))
    l3.append(a)
    if len(l3)==2:
        l2.extend(l3[::-1])
        l3=[]
if len(l3)%2:
    l2.append(l3[-1])
print(*l2)