

list1=[13,45,48,74,53,85,29,19,17,29,86,48,4,6,53,59,68,61]

a=[0]

for i in list1:
    if i>a[0]:
        a.insert(0,i)

print("Maximum number in list =",a[0])