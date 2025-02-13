


a="@#$%Cricket is the famous game on Cricket we have 1 2 3 4 6 runs and 100 runs is important"
e=len(a)
print(e)
b=0
c=0
d=0

for i in a:
    if i.isalpha():
        b+=1

for i in a:
    if i.isnumeric():
        c+=1

for i in a:
    if i.isspace():
        d+=1

print(b)
print(c)
print(d)

No_splcharacter=e-b-c-d
print(No_splcharacter)