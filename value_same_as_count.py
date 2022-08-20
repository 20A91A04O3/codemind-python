n=int(input())
l=list(map(int,input().split()))
dic={}
c=0
for i in l:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in dic.items():
    if k==v:
        c+=1
print(c)