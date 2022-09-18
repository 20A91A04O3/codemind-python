n=int(input())
s=str(n)
l=[]
for i in s:
    s1=1
    for j in range(int(i),0,-1):
        s1*=j
    l.append(s1)


if sum(l)==n:
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")