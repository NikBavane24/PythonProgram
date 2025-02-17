


a="Cricket is the famous game Cricket help me to be physical fit and famous"

b=a.lower().split()

check="e"

c=[]

for i in b:
    if (i.find(check)==-1):
        print(i)
        c.append(i)

print("List of matching last letter as e=",c)



