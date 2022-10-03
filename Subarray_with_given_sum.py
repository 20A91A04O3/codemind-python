t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l1=[]
    for i in range(0,len(l)+1):
        for j in range(i+1,len(l)+1):
            if sum(l[i:j])==k:
                l1.append(i+1)
                l1.append(j)
                break
    if len(l1)!=0:
        print(*l1[0:2])
    else:
        print(-1)