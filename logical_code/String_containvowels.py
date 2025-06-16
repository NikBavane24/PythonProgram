


s = "Geeksforyouriam"
v = 'aeiou'
s=s.lower()

if all(i in s for i in v):
    print("True")
else:
    print("False")