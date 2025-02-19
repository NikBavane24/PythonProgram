import re

a="Cricket is the famous game Cricket help me to be physical fit and famous"

pattern=r'f\w*t\b'

matches=re.findall(pattern,a)

print("List of matching 1st letter as f=",matches)