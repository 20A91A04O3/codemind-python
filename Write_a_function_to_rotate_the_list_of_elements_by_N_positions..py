n=int(input())
l=list(map(int,input().split()))
t=int(input())
for i in range(t):
    s=l.pop(-1)
    l.insert(0,s)
print(*l)
    