s=input()
l1=[]
l2=[]
if s==s[::-1]:
    print(s)
else:
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            s1=s[i:j]
            if s1==s1[::-1]:
                l1.append(s1)
                l2.append(len(s1))
    for i in l1:
        if max(l2)==len(i):
            print(i)
            break
        