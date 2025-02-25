

s="Cricket is the famous game. Cricket help me to be physical fit and famous"

freq={}

for char in s:
    freq[char]=freq.get(char,0)+1
    print(freq)

max_Ch=max(freq)

print(max_Ch)