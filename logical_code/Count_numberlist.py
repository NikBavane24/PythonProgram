

a=[13,45,48,74,53,85,29,13,19,17,29,86,3,53,59,68,13,61,-11,-13,-43,-56,-28,19,-24,-88,13,-35,-97,-81]
b=a.count(13)
print(b)

c=a.count(19)
print(c)

count=0

for i in a:
    if i==13:
        count+=1

print("Count of number 13=",count)


print("Count of number 19=",a.count(19))

