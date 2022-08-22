n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(1,n,2):
    for j in range(l[i]):
        l1.append(l[i-1])
print(*l1)
