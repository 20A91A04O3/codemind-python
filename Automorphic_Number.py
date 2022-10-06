n=int(input())
n2=n**2
s1=str(n)
s2=str(n2)
s3=s2[len(s1):]
if s3==s1:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")