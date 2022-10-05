t=int(input())
for i in range(t):
    n=int(input())
    for i in range(n):
        if (i*i)==n:
            print(True)
            break
    else:
        print(False)
    