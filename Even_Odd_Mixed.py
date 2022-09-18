n=int(input())
s=str(n)
ec=0
oc=0
for i in s:
    if int(i)%2==0:
        ec+=1
    else:
        oc+=1
if ec==len(s):
    print("Even")
elif oc==len(s):
    print("Odd")
else:
    print("Mixed")
