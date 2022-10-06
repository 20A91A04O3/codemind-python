s=input()
n=int(s)
s2=0
for i in range(0,len(s)):
    s1=int(s[i])**(i+1)
    s2+=s1

if n==s2:
    print(True)
else:
    print(False)