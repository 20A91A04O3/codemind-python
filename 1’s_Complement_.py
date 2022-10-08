n=int(input())
s=list(bin(n)[2:])
for i in range(len(s)):
    if s[i]=="0":
        s[i]="1"
    elif s[i]=="1":
        s[i]="0"
s=''.join(s)
print(int(s,2))
