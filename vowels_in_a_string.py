s=input()
ele=input()
v="aeiouAEIOU"
if ele in s:
    if ele in v:
        print(True)
        print(s.index(ele))
else:
    print(False)