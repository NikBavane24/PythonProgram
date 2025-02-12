

a=[13,45,48,74,53,85,29,19,17,29,86,3,48,53,59,68,61]

a.sort()
print("Smallest number in list =",a[0])

smallest=a[0]

for val in a:
    if val<smallest:
        smallest=val

print("Smallest number in list =",smallest)