n=input()
k=[]
for i in n:
    k.append(i)
s=list(set(k))
c=0
for i in s:
    if k.count(i)%2==0 :
        c=c+1
if(c==len(s) or c==len(s)-1):
    print("Valid String")
else:
    print("Not Valid")