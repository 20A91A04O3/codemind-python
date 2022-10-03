t=int(input())
for i in range(t):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l3=[]
    for i in range(1,n+1):
        if (i in l1[1:]) or (i in l2[1:]):
            l3.append(i)
    if len(l3)==n:
        print("YES")
    else:
        print("NO")
    