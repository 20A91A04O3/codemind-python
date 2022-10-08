from math import *
n=int(input())
for i in range(1,int(sqrt(n))+5):
    if (2**i)==n:
        print(True)
        break
else:
    print(False)
