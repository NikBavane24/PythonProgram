from collections import Counter

a= 'The city was bustling with activity as people hurried to and fro, going about their daily routines.'
b=a.replace(" ","_")

fre=Counter(b)
print(fre)

Max=max(fre,key=fre.get)
print(Max)
Min=min(fre,key=fre.get)
print(Min)

c=b.split()

