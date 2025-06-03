

a="Cricket is the famous game Cricket help me to be physical fit and famous"

b=a.split()
c=b[0]
for word in b:
    if len(word)>len(c):
        c=word

print(c)


