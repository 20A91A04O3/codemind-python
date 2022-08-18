n=int(input())
l=list(map(int,input().split()))
l1=l[::-1]

sum=0
for i in range(len(l)):
    if l1[i]==1:
        sum=sum+(2**i)
    else:
        continue
print(sum)