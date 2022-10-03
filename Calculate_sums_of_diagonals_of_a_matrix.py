r=int(input())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
m1=m[::-1]
s1=0
s2=0
for i in range(r):
    for j in range(len(m)):
        if i==j:
            s1+=m[i][j]
for i in range(r):
    for j in range(len(m1)):
        if i==j:
            s2+=m1[i][j]
print('Principal Diagonal:{}'.format(s1))
print('Secondary Diagonal:{}'.format(s2))    