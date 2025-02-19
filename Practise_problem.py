from collections import Counter

#count the number of words in sentence
a="Cricket is the famous game. Cricket help me to be physical fit and famous"

a=a.lower()

b=a.count("c")
print("c=",b)

#find biggest word in the sentence

c=a.split()
print(c)
d="game"

for word in c:
    if len(word)>len(d):
        d=word
        print(word)
print(d)

count=0

for i in c:
    count+=1

print(count)



