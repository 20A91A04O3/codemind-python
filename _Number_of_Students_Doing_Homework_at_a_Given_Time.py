n=int(input())
l=list(map(int,input().split()))
m=int(input())
l1=list(map(int,input().split()))
s=int(input())
c=0
for i in range(len(l)):
    if (s>=l[i] and s<=l1[i]):
        c+=1
print(c)
