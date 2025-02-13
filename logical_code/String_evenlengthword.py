

a="Cricket is the famous game Cricket help me to be physical fit and famous"
c=a.count("m")
print(c)

b=a.split()

for i in b:
    if len(i)%2==0:
        print(i,"=Even length word")

    else:
        print(i,"=odd length word")