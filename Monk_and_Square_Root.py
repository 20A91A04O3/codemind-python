n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    for i in range(b):
        if (i*i)%b==a:
            print(i)
            break
    else:
        print(-1)