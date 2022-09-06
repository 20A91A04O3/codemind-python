s1=input()
s2=input()
s3=s1.lower()
s4=s2.lower()
l1=[]
for i in s3:
    if i.isalpha():
        if i in s4:
            l1.append(i)
l2=sorted(set(l1))
print(len(l2))
