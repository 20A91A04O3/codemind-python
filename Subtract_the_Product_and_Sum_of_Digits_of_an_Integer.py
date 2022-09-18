n=int(input())
s=str(n)
sum=0
mul=1
for i in s:
    sum+=int(i)
    mul*=int(i)
print(mul-sum)    