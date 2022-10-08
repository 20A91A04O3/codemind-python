n=int(input())
l=list(map(int,input().split()))
s=list(set(l))
for i in s:
    if l.count(i)==1:
        print(i)
        break