n=int(input())
l=list(map(int,input().split()))
l1=l[::-1]
c=0
if len(l)%2:
    c+=1
for i in range(len(l)//2):
    print(l[i],l1[i],end=' ')
if c==1:
    print(l[(len(l)//2)],0)