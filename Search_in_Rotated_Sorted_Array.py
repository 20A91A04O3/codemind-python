n=int(input())
l=list(map(int,input().split()))
s=int(input())
if s in l:
    print(l.index(s))
else:
    print(-1)
