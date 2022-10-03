n=int(input())
l=list(map(int,input().split()))
l1=sorted(l)
for i in range(1,max(l1)+1):
    if i not in l1:
        print(i)
        break
else:
    print(max(l1)+1)
