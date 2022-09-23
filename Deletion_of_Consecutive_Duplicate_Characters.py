t=int(input())
for i in range(t):
    s=input()
    c=0
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            c+=1
    print(c)