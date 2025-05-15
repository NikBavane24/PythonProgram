

a=list(range(1,11))
print(a)
a[0],a[-1]=a[-1],a[0]
#a[3],a[5]=a[5],a[3]
b=len(a)

print("List after first and last element interchange",a)
print("length of list a=",b)