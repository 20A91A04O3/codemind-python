n=int(input())
l=list(map(int,input().split()))
sum=0
for i in l:
    if i%2!=0:
        sum+=i
    else:
        break
print(sum)
    