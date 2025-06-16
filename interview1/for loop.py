import sys

a=[10,20,30]
for i in a:
    print(i)
else:
    print("Out of for loop")

print(sys.version)

r="dghnvcddfgh"
y=r
print("X=",sys.getrefcount(r))