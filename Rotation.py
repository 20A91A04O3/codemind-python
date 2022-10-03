t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(s):
        s1=l.pop(-1)
        l.insert(0,s1)
    print(*l)