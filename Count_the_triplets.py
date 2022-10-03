t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if ((l[i]+l[j]) in l):
                c+=1
    if c!=0:
        print(c)
    else:
        print(-1)