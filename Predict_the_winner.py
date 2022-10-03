n=int(input())
l=list(map(int,input().split()))
l1=[]
if sum(l)%4==0:
    print("X")
else:
    print("Y")