n=input()
s=list(set(n))
l1=[]
l1.append(n.count("("))
l1.append(n.count(")"))
l1.append(n.count("["))
l1.append(n.count("]"))
l1.append(n.count("{"))
l1.append(n.count("}"))
c=0
d=0
#print(l1)
for i in range(1,len(l1),2):
    if l1[i]==l1[i-1]:
        c+=1
    else:
        d+=1
if c>0 and d==0:
    print(True)
else:
    print(False)
    

