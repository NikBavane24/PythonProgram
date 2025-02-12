from collections import Counter

a="Cricket is the famous game. Cricket help me to be physical fit and famous"

w_freq=Counter(a.split())

print(w_freq)
print(min(w_freq))