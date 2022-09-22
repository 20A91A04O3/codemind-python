n=int(input())
l=list(map(int,input().split()))
s=int(input())
l1=[]
if s not in l:
    print(-1,-1)
else:
    for i in range(len(l)):
        if l[i]==s:
            l1.append(i)
print(l1[0],l1[-1])