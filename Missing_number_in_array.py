t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    for i in range(min(l),max(l)+1):
        if i not in l:
            print(i)
            break
    else:
        print(l[-1]+1)
        
