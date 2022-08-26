n=int(input())
l=list(map(int,input().split()))
s=list(set(l))
l1=sorted(s)
if l==l1:
    print("yes")
else:
    print("no")
