from collections import Counter

a="Cricket is the famous game Cricket help me to be physical fit and famous"
b=a.replace(" ","_")
print(b)

freq=Counter(b)

print(freq)

max_char=max(freq,key=freq.get)

print("Maximum time character repeats",max_char)

min_char=min(freq,key=freq.get)
print("Minimum time character repeats",min_char)

Char_e=freq.get("e")
print(Char_e)