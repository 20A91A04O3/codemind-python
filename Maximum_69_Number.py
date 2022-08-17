s=input()
l=list(s)
s1=''
for i in range(len(s)):
    if s[i]=="6":
        l[i]='9'
        break
for i in l:
    s1=s1+i
print(s1)