s=int(input())
for i in range(s):
    n,a,b,k=map(int,input().split())
    c,d=0,0
    for i in range(1,n+1):
        if (i%a==0) and (i%b!=0):
            c+=1
            if (c+d)>=k:
                print("Win")
                break
        elif (i%b==0) and (i%a!=0):
            d+=1
            if (c+d)>=k:
                print("Win")
                break
    else:
        print("Lose")
