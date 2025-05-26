from collections import Counter



def character_count(a):
    a=a.replace(" ","_")
    frequency=Counter(a)
    print(frequency)
    print(max(frequency,key=frequency.get))
    print(min(frequency,key=frequency.get))
    print(frequency.get("c"))

character_count("The Counter class from the collections module helps count the occurrences of characters.")