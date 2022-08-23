s=(input())
v="aeiou"
l=[]
l2=[]
for i in s:
    if (i in v) :
        if i not in l:
            l.append(i)
for j in v:
    if j not in l:
        l2.append(j)
if len(l)!=5:
    print(*l2)
elif len(l)==5:
    print(0)
    