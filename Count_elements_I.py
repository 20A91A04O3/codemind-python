m,n=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s1=set(l1)
s2=set(l2)
c=0
for i in s1:
    if i in s2:
        c+=1
print(c)