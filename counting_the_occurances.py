s=input()
s1=input()
s=s.split()
s=''.join(s)
if s1 in s:
    print(s.count(s1))
else:
    print(-1)
