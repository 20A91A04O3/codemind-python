n=int(input())
for i in range(n):
    s=input()
    s1=(int(s,2))
    s2=str(oct(s1))
    s3=s2[2:]
    print(s3)