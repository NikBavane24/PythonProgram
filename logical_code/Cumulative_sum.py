

a = [1, 2, 3, 1, 2, 4, 5, 6, 5]

b=sum(a)
print("Cumulative sum of list=",b)

c=0
for i in a:
    if i==5:
        continue
    c+=i

print("Cumulative sum of list=",c)