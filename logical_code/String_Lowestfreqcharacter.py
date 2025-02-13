from collections import Counter



a="Cricket is the famous game Cricket help me to be physical fit and famous"

freq= Counter(a)
print(freq)
res=min(freq, key=freq.get)
res1=max(freq,key=freq.get)

print(str(res))
print(str(res1))
