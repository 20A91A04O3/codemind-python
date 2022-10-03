n=int(input())
l=list(map(int,input().split()))
s=list(set(l))
l1=[]
for i in s:
    l1.append(l.count(i))
l2=l1.index(max(l1))
print(s[l2])
