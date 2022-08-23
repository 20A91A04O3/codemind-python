n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    s=str(i)
    s1=s[::-1]
    if s==s1:
        l1.append(s1)
print(len(l1))
