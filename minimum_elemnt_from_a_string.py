s=input()
l=s.split()
l1=l[-1]
l2=[]
l3=[]
for i in l1:
    if i.isupper():
        l2.append(i)
    else:
        l3.append(i)
if (min(l3).upper()) in l2:
    print(min(l3))
else:
    print(min(l1))