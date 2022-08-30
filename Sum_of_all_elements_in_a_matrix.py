r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
sum1=0
for i in m:
    sum1+=sum(i)
print(sum1)