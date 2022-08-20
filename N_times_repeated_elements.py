n=int(input())
l=list(map(int,input().split()))
a=int(input())
dic={}
l1=[]
for i in l:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in dic.items():
    if a==v:
        l1.append(k)
if len(l1)!=0:
    print(*l1)
else:
    print(-1)