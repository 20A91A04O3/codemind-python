n=int(input())
l=list(map(int,input().split()))
l1=l[0:n//2]
l2=l[n//2:]
l3=l1+l2
for i in range(len(l1)):
    print(l3[i],l2[i],end=' ')