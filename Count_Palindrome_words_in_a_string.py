s=input()
l1=s.lower()
l=l1.split()
c=0
for i in l:
    s1=i[::-1]
    if i==s1:
        c+=1
print(c)