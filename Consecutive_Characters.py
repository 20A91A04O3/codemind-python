s=input()
l=[]
c=0
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        c+=1
    else:
        l.append(c)
        c=0
else:
    l.append(c)
print(max(l)+1)
