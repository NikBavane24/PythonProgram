import re

a=" Hello! 123@ jAvA_"
b=0
c=0
d=0
for i in a:
    if i.isalpha():
        b=b+1
print(b)

for i in a:
    if i.isspace():
        c=c+1
print(c)

for i in a:
    if i.isnumeric():
        d=d+1
print(d)

lower_case=re.findall(r"[a-z]",a)
print(len(lower_case),lower_case)

Upper_case=re.findall(r"[A-Z]",a)
print(len(Upper_case),Upper_case)

Numeric_case=re.findall(r"[0-9]",a)
print(len(Numeric_case),Numeric_case)

Special_case=re.findall(r"[!@#$%^&*()_]",a)
print(len(Special_case),Special_case)