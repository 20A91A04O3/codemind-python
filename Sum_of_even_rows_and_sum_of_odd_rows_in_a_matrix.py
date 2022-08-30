r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
es=0
os=0
for i in range(len(m)):
    if i%2==0:
        es=es+(sum(m[i]))
    else:
        os=os+(sum(m[i]))
print(es,os)
        