n=int(input())
l=[]
for i in range(n):
    s=int(input())
    l.append(s)
t=int(input())
c=0
for i in l:
    if i<=t:
        c+=1
    else:
        c+=2
print(c)