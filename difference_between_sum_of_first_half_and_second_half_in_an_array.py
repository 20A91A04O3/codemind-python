n=int(input())
l=list(map(int,input().split()))
l1=l[0:(n//2)]
l2=[]
for i in l:
    if i not in l1:
        l2.append(i)
print(abs(sum(l2)-sum(l1)))