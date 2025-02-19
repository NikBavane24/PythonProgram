from collections import Counter

a="Cricket is the famous game. Cricket help me to be physical fit and famous famous"
b=a.split()
w_freq=Counter(b)

print(w_freq)

Mi=min(w_freq,key=w_freq.get)
print(Mi)

Mx=max(w_freq,key=w_freq.get)
print(Mx)