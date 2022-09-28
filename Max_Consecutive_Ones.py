n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in l:
    if i==1:
        c+=1
    else:
        if c>d:
            d=c
            c=0
else:
    if c>d:
        d=c
print(d)