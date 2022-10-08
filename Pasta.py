n,m=map(int,input().split())
a1=list(map(int,input().split()))
a2=map(int,input().split())
c=0
for i in a2:
    if i in a1:
        c+=1
        a1.remove(i)
if c==m:
    print("Yes")
else:
    print("No")
