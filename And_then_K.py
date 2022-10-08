for i in range(int(input())):
    n=int(input())
    s1=n
    for i in range(1,n):
        a=n-1
        n=n&(n-i)
        if n==0:
            print(a)
            break
    else:
        print(0)
        