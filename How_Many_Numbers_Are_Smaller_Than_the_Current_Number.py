n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    c=0
    for j in l:
        if i>j:
            c+=1
    l1.append(c)
print(*l1)
