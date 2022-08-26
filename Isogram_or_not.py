s=input()
s1=s.lower()
c=0
for i in s1:
    if s1.count(i)==1:
        c+=1
if c==len(s1):
    print(True)
else:
    print(False)