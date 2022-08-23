n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    c=0
    while(i>0):
        r=i%10
        c+=1
        i=i//10
    l1.append(c)
e=l1.count(min(l1))
print(e)