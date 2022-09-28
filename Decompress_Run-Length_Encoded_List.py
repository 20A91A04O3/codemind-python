n=int(input())
l=list(map(int,input().split()))
s=''
for i in range(0,len(l),2):
    j=i+1
    s1=str(l[j])
    s+=(s1*l[i])
for i in s:
    print(i,end=' ')
