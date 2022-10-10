n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(1,min(l)+1):
    c=0
    for j in l:
        if j%i==0:
            c+=1
        if c==len(l):
            l1.append(i)
            break
print(max(l1))       