s1=input()
s2=input()
s1.lower()
s2.lower()
s1=s1.split()
s2=s2.split()
c=0
for i in s1:
    for j in s2:
        if i.lower()==j.lower():
            c+=1
print(c)


