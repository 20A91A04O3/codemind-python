m=int(input())
n=int(input())
l1=[]
for i in range(m):
    l=list(map(int,input().split()))
    l1.append(sum(l))
print(sum(l1))
