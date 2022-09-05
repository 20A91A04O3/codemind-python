n=int(input())
m=int(input())
sum1=0
sum2=0
for i in range(1,(n//2)+1):
    if n%i==0:
        sum1+=i
for j in range(1,(m//2)+1):
    if m%j==0:
        sum2+=j

if sum1==m and sum2==n:
    print("Amicable")
else:
    print("Not Amicable")