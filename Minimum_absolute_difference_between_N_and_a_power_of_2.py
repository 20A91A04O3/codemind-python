n=int(input())
l1=[]
l2=[]
for i in range(1,n*2):
    if (2**i)<=n:
        l1.append(2**i)
    else:
        l2.append(2**i)
        break
if n in l1:
    print(0)
else:
    if abs(l1[-1]-n)<abs(l2[0]-n):
        print(abs(l1[-1]-n))
    else:
        print(abs(l2[0]-n))