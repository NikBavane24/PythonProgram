import re

a="Java"

Lcase=re.findall(r"[a-z]",a)
print(Lcase)

Ucase=re.findall(r"[A-Z]",a)
print(Ucase)

b="java"

c="A very good morning"

if a==b:
    print("Both the string are same")

else:
    print("Both the string are different")

d=c[2:8]
print(d)

e=c[::-1]
print(e)

f=c[-7::1]
print(f)