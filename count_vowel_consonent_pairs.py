s=input()
v='aeiouAEIOU'
c=0
for i in range(len(s)):
    if s[i].isalpha()==False or s[len(s)-i-1].isalpha()==False:
        continue
    elif ((s[i]in v )and(s[len(s)-i-1]not in v))or((s[i]not in v )and(s[len(s)-i-1] in v)):
        c+=1
print(c//2)