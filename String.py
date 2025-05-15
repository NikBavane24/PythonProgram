from collections import Counter

a= 'The city was bustling with activity as people hurried to and fro, going about their daily routines.'
b=a.replace(" ","_")

freq=Counter(b)
print(freq)

Max=max(freq,key=freq.get)
print(Max)
Min=min(freq,key=freq.get)
print(Min)

c=b.split()

