s=input()
l=s.split()
v="aeiouAEIOU"
l1=[]
for i in l:
    c=0
    if (i[0] in v) and (i[-1] not in v):
        c=1
    l1.append(c)
print(sum(l1))