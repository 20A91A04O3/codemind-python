s=input()
s1=s.lower()
l1=s1.split()
l2=''.join(l1)
l3=[]
for i in l2:
    if l2.count(i)==1:
        l3.append(i)
l3.sort()
s4=''.join(l3)
print(s4)