import re

a="Hello! 123 Bye 789"

b=a.replace(" ","_",2)
print(b)

res=re.sub(r'\d'," ",a)

print(res)

c=re.split(" ",a)
print(type(c),c)

d=a.split()
print(d)