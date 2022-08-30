r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
es=0
os=0
for j in m:
    for k in j:
        if k%2==0:
            es+=k
        else:
            os+=k
print(es,os)        