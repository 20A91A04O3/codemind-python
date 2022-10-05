n=int(input())
mul=1
sum=0
s=str(n)
for i in s:
    mul*=int(i)
    sum+=int(i)
if mul==sum:
    print("Spy Number")
else:
    print("Not Spy Number")
    