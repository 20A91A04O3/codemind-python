a,b=map(int,input().split())
l=list(map(int,input().split()))
for i in range(b):
    s=l.pop(0)
    l.append(s)
print(*l)
