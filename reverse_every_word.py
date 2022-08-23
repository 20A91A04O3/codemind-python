s=(input())
l=s.split()
l1=[]
for i in l:
    s1=i
    l1.append(s1[::-1])
print(*l1)