from collections import Counter



def character_count(a):
    a=a.replace(" ","_")
    frequency=Counter(a)
    print(frequency)
    print(max(frequency,key=frequency.get))
    print(min(frequency,key=frequency.get))
    print(frequency.get("t"))

character_count("The Counter class from the collections module helps count the occurrences of characters.")
print("-------------------------------------------------------------------")
a="The Counter class from the collections module helps count the occurrences of characters."
t=0
for word in a:
    if word=="t":
        t=t+1
print(t)