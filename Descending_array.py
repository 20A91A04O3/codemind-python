n=int(input())
l=list(map(int,input().split()))
l1=l[::-1]
l.sort()
if l==l1:
    print("yes")
else:
    print("no")