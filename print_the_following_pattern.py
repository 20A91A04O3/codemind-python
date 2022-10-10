n=int(input())
for i in range(n):
    s=''
    for j in range(n):
        if i==j:
            s+="0"
        else:
            s+="x"
    print(s)