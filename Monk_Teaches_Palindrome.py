t=int(input())
for i in range(t):
    s=input()
    s1=s[::-1]
    if s==s1 and (len(s)%2==0):
        print("YES EVEN")
    elif s==s1 and (len(s)):
        print("YES ODD")
    else:
        print("NO")