from collections import Counter



List = [2, 1, 2, 2, 1, 3]

frequ=Counter(List)
print(frequ)

max_count=max(frequ,key=frequ.get)
print(max_count)

min_count=min(frequ,key=frequ.get)
print(min_count)

count1=frequ.get(1)
print(count1)