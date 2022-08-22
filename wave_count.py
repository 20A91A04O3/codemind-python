n=int(input())
l=list(map(int,input().split()))
c=0
c1=0
for i in range(1,n-1,2):
    if l[i]>l[i+1] and l[i]>l[i-1]:
        c+=1
    else:
        c1+=1
if c1==0:
    print(c)
else:
    print(-1)