s=input()
l=s.split()
s1=''.join(l)
c=s1.count(min(s1))
c1=s1.count(max(s1))
print(min(s1),c,max(s1),c1)