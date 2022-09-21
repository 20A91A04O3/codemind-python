n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(1,max(l)):
    if (i*i) in l:
        l1.append(i*i)
print(sum(l1))
