n=int(input())
l=list(map(int,input().split()))
l2=[]
for i in l:
    if i!=0:
        l2.append(i)
s1=l.count(0)
while(s1>0):
    l2.append(0)
    s1-=1
print(*l2)
