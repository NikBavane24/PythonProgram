from os import remove

a=[13,45,48,74,53,85,29,13,19,17,29,86,3,53,59,68,13,61,-11,-13,-43,-56,-28,-24,-88,13,-35,-97,-81]


remo1=[45,29,3,-11,-56]

b=[]

for i in a:
    if i not in remo1:
        b.append(i)

print("After remove element, list is",b)
