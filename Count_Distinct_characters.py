s=input()
s1=s.lower()
l1=s1.split()
l2=''.join(l1)
l3=[]
for i in l2:
    if i not in l3:
        l3.append(i)
print(len(l3))