n=int(input())
for i in range(n):
    a=int(input())
    b=str(bin(a))
    l=[]
    l.append(int(b[2:]))
    print(*l)
