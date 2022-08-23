n=int(input())
l=list(map(int,input().split()))
sum=0
for i in l:
    while(i>9):
        r=i%10
        sum+=r
        i=i//10
    else:
        sum+=i
print(sum)
