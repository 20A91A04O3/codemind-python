a,b,c=map(int,input().split())
cap=2*a*b*c*512
s=str(cap//1024)
print(s+"KB")
