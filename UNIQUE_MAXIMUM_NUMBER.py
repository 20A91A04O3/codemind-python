n=int(input())
l=list(map(int,input().split()))
s1=list(set(l))
l1=[]
for i in s1:
    if l.count(i)==1:
        l1.append(i)
if len(l1)!=0:
    print(max(l1))
else:
    print(-1)