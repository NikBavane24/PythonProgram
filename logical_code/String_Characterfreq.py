from collections import Counter

a="Cricket is the famous game Cricket help me to be physical fit and famous"
b=a.replace(" ","_")
print(b)

freq=Counter(b)

print(freq)

max_char=max(freq,key=freq.get)

print(max_char)