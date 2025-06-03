from collections import Counter

s="Cricket is the famous game. Cricket help me to be physical fit and famous"
freq=Counter(s)
print(freq)

max_ch = max(freq, key=freq.get)
print("Max charcter=",max_ch)

min_ch=min(freq,key=freq.get)
print("Min charcter=",min_ch)

char_C= freq.get("C")
print("Frequency of C=",char_C)