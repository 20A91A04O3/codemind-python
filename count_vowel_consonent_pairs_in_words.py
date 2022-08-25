s=input()
l=s.split()
v='aeiouAEIOU'
c=0
for i in l:
    for j in range(len(i)):
        if ((i[j] in v) and (i[len(i)-j-1] not in v)):
            c+=1
print(c)