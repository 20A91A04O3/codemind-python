s1=input()
s2=input()
l1=s1.lower()
l2=s2.lower()
s3=''
for i in l1:
    if  i in l2:
        s3=s3+i
if len(s1)==len(s3):
    print(True)
else:
    print(False)