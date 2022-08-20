n=int(input())
l=list(map(int,input().split()))
dic={}
l1=[]
for i in l:
    if i%2==0:
        if i not in l1:
            l1.append(i)
print(sum(l1))