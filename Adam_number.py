n1=int(input())
s=str(n1)
s1=s[::-1]
n2=int(s1)
sq1=n1*n1
sq2=n2*n2
s3=str(sq2)
if str(sq1)==s3[::-1]:
    print(True)
else:
    print(False)