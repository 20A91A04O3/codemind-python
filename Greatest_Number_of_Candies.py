n=int(input())
l=list(map(int,input().split()))
s=int(input())
l1=[]
for i in l:
    if (i+s)>=max(l):
        l1.append(True)
    else:
        l1.append(False)
print(*l1)

