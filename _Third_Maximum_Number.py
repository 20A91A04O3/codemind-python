n=int(input())
l=list(map(int,input().split()))
l1=sorted(list(set(l)))
if len(l1)<3:
    print(max(l1))
else:
    print(l1[-3])