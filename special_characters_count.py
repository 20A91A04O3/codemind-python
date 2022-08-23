s=input()
c=0
for i in s:
    if (i.isalpha()!=True) and(i.isdigit()!=True) and i!=" ":
        c+=1
print(c)