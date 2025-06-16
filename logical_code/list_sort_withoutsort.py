
a = [10, 24, 76, 23, 12,4,6,15,18,25,35,48,52,67]
n=len(a)
print(n)

for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]

print(a)
print(a[-2])