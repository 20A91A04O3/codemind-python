n=int(input())
l=list(map(int,input().split()))
l1=l[0:n//2]
l2=l[n//2:][::-1]
l3=l2+l1
print(*l3)

