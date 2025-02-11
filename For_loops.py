

a=[1,2,3,4,5,6]

print(type(a))

for x in a:
    print(x)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
for i in range(1,11):
    if i==9:
        continue
    #if i==10:
        #break
    print(i)

else:
    print("For loop end")