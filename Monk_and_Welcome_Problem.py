n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in range(n):
    l1[i]=l1[i]+l2[i]
print(*l1)