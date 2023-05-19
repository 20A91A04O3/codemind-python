r,c=map(int,input().split())
m=[[0]*r]*c
for i in range(r):
    m[i]=list(map(int,input().split()))
s1=0
for i in range(0,r):
    for j in range(0,c):
        if(i==j or (i+j)==r-1):
            s1+=m[i][j]
print(s1)
