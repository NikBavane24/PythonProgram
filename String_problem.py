import re

a="A paragraph is a group of sentences that develops a single 123456789 idea It can !@#$5%^6 be a section of a longer piece of writing or it can be a short composition by itself"

b=len(a)
print(b)

c=0
d=0
e=0
for i in a:
    if i.isalpha():
        c+=1
print("Alphabet=",c)

for i in a:
    if i.isspace():
        d+=1
print("Spaces =",d)

for i in a:
    if i.isnumeric():
        e+=1
print("Numeric =",e)

Specialchar= b-c-d-e
print("Special_char",Specialchar)


cap=re.findall("A_Z")
print(cap)
