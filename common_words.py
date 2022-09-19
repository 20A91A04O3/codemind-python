s1=input()
s2=input()

s1=s1.split()
s2=s2.split()
l1=[]
for i in s2:
    for j in s1:
        if i.lower()==j.lower():
            l1.append(i)
print(' '.join(l1))