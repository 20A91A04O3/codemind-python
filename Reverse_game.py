n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    s=str(i)
    s1=s[::-1]
    l1.append(int(s1))
print(*l1)

