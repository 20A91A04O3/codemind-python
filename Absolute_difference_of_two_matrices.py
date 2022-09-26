r=int(input())
l1=[]
l2=[]
for i in range(r):
    l=list(map(int,input().split()))
    l1.append(l)
for i in range(r):
    l=list(map(int,input().split()))
    l2.append(l)
l3=[]
for i in range(len(l1)):
    l4=[]
    for j in range(len(l1)):
        s1=(abs(l1[i][j]-l2[i][j]))
        l4.append(s1)
    l3.append(l4)
for i in l3:
    print(*i)

    