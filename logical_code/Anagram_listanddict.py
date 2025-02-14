


a = ['bat', 'nat', 'tan', 'ate', 'eat', 'tea']
dict={}
for word in a:
    sort_word=''.join(sorted(word))
    print(sort_word)

    if sort_word in dict:
        dict[sort_word].append(word)

    else:
        dict[sort_word]=[word]

res = list(dict.values())
print(res)