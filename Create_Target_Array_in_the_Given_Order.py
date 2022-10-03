n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
l3=[]
for i in range(n):
    l3.insert(l2[i],l1[i])
print(*l3)