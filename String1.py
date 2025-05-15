from collections import Counter

a="a paragraph is a group of sentences that develops a single 123456789 idea It can !@#$5%^6 be a section of a longer piece of writing or it can be a short composition by itself"
b=a.replace(" ","_")
print(b)
Freq= Counter(b)
print(Freq)
c=0
for i in b:
    if i=="_":
        c+=1

print("Character _ comes this much times=",c)

d=a.split()
e=a[0]
for i in d:
    if len(i)>len(e):
        e=i
print(e)

Freq= Counter(d)
print(Freq)

Max=max(Freq,key=Freq.get)
print(Max)

Min=min(Freq,key=Freq.get)
print(Min)