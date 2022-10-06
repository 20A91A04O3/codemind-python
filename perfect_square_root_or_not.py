n=int(input())
l=[]
for i in range(n):
    l.append(i*i)
if n in l:
    print(True)
else:
    print(False)