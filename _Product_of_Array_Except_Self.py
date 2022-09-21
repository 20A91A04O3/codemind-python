n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    s=1
    for i in l:
        s=s*i
    for i in l:
        print(s//i,end=" ")