'''def octal(s):
    if i=="0":
        return "0000"
    elif i=="1":
        return "0001"
    elif i=="2":
        return "0010"
    elif i=="3":
        return "0011"
    elif i=="4":
        return "0100"
    elif i=="5":
        return "0101"
    elif i=="6":
        return "0110"
    elif i=="7":
        return "0111"
    elif i=="8":
        return "1000"
    elif i=="9":
        return "1001"
    elif i=="A":
        return "1010"
    elif i=="B":
        return "1011"
    elif i=="C":
        return "1100"
    elif i=="D":
        return "1101"
    elif i=="E":
        return "1110"    
    elif i=="F":
        return "1111"
t=int(input())
for i in range(t):
    n=input()
    s1=''
    for i in n:
        s1+=octal(i)
    print(s1)
'''
for i in range(int(input())):
    n=input()
    bn=bin(int(n,16)).replace("ob","")
    bn=bn[2::]
    bn=list(bn)
    if n[0]=="0":bn.insert(0,"0000")
    if n[0]=="1":bn.insert(0,"000")
    if n[0]=='2' or n[0]=="3":bn.insert(0,"00")
    if n[0]=="4" or n[0]=="5" or n[0]=="6" or n[0]=="7":bn.insert(0,"0")
    a=""
    a=''.join(bn)
    print(a)