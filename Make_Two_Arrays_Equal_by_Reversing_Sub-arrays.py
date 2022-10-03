n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
l1=sorted(l1)
l2=sorted(l2)
if l1==l2:
    print(True)
else:
    print(False)