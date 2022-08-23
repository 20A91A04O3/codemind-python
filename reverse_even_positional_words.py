s=(input())
l=s.split()
l2=[]
for i in range(len(l)):
    if i%2==0:
        s1=l[i]
        l2.append(s1[::-1])
    else:
        l2.append(l[i])
print(*l2)