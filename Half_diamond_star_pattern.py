n=int(input())
if n>=3 and n<=100:
    for i in range(1,n+1):
        s=''
        for j in range(i):
            s+="*"
        print(s)
    for i in range(n-1,0,-1):
        s1=''
        for j in range(i):
            s1+="*"
        print(s1)
else:
    print("The pattern is not possible")
