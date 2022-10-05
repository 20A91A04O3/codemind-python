a=int(input())
b=int(input())
l1=[]
for i in range(a,b+1):
    s=str(i)
    s1=s[::-1]
    if s==s1:
        l1.append(s)
print(*l1)
