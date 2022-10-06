n=int(input())
a=0
b=1
c=0
for i in range(n):
    c=a+b
    if c==n:
        print(True)
        break
    else:
        a=b
        b=c
        c=0
else:
    print(False)
    