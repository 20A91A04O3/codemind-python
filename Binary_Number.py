n=int(input())
for i in range(0,((2**n)-1)+1):
    s=bin(i)[2:]
    if len(s)==n:
        print(s)
    else:
        s=list(s)
        while(len(s)<n):
            s.insert(0,"0")
        print(''.join(s))
    