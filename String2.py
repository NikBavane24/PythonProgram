import re
from collections import Counter

a="Cricket is the famous game. Cricket help me to be physical fit and famous"

pattern=r'f\w*t\b'

word=re.findall(pattern,a)
print(word)

fr=Counter(a)
print(fr)

Char_m=fr.get(" ")
print(Char_m)

Min=min(fr,key=fr.get)
print(Min)
b=0
for i in a:
    if i.isspace():
        b+=1

print(b)