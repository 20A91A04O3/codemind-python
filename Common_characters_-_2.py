s1=input()
s2=s1.lower()
s3=s2.split()
s4=''.join(s3)
s5=set(s4)
l=''
for i in s5:
    c=0
    for j in s3:
        if i in j:
            c+=1
            if c==len(s3):
                s=s3[0].count(i)
                se=s*i
                l+=se
                break
if len(l)!=0:
    print(len(l))
else:
    print(0)


