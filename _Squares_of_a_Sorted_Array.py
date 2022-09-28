n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if l[i]<0:
        l[i]=abs(l[i])
l2=sorted(l)
l1=[]
for i in l2:
    l1.append(abs(i)**2)
print(*l1)     
        