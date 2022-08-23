s=(input())
l=s.split()
l2=[]
for i in range(len(l)):
    s1=l[i]
    l2.append(s1[::-1])
print(*l2[::-1])