s=input()
l=s.split()
l1=[]
for i in l:
    l1.append(len(i))
print(max(l1))