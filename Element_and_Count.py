n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i not in l1:
        l1.append(i)
        c=l.count(i)
        l2.append(c)
for i in range(len(l1)):
    print(l1[i],l2[i],end=' ')