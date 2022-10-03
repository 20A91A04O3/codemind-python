t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l3=sorted(l1+l2)
    print(*l3)
    