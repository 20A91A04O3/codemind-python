a,b=map(int,input().split())
l1=[]
l2=[]
for i in range(1,a*2):
    l1.append(a*i)
for j in range(1,b*2):
    l2.append(b*j)
l3=[]
for i in l1:
    if i in l2:
        print(i)
        break