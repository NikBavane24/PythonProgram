import re

a="Cricket is the famous game. Cricket help me to be physical fit and famous"

pattern=r'\w*e\b'

word=re.findall(pattern,a)
print(word)