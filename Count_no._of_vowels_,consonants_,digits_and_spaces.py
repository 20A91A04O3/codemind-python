s=input()
s1=s
s=s.split()
s=''.join(s)
v="AEIOUaeiou"
vc=0
cc=0
dc=0
wc=s1.count(" ")
for i in s:
    if i.isalpha():
        if i in v:
            vc+=1
        else:
            cc+=1
    elif i.isdigit():
        dc+=1

print("Vowels:".format(),vc)
print("Consonants:".format(),cc)   
print("Digits:".format(),dc)
print("White spaces:".format(),wc)
