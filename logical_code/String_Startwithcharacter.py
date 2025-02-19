import re

a="Cricket is the famous game Cricket help me to be physical fit and famous"

b=a.lower().split()

check="e"

c=r'\w*s\b'
d=re.findall(c,a)
print(d)



