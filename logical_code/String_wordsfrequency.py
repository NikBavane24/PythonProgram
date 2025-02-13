from collections import Counter

a="Cricket is the famous game. Cricket help me to be physical fit and famous"
b=a.split()
w_freq=Counter(b)

print(w_freq)
print(min(w_freq))