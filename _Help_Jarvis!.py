t=int(input())
for i in range(t):
    n=int(input())
    s=list(str(n))
    s=sorted(s)
    c=1
    for i in range(1,len(s)):
        if abs(int(s[i])-int(s[i-1]))==1:
            c+=1
    if c==len(s):
        print("YES")
    else:
        print("NO")
    