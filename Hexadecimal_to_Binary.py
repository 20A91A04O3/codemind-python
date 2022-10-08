
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