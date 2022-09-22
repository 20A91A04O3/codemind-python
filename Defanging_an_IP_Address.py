s=input()
l=list(s)
for i in range(len(l)):
    if l[i]=='.':
        l[i]="[.]"
print(''.join(l))