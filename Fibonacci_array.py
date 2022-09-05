n=int(input())
l=list(map(int,input().split()))
c=2
for i in range(2,len(l)):
    j=i-1
    k=i-2
    if l[j]+l[k]==l[i]:
        c+=1
if c==len(l) and len(l) > 2:
    print("yes")
else:
    print("no")

    
    


