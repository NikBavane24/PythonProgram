

lst = [1, 2, 3, 4, 5]
str_lst = list(map(str, lst))
print(type(str_lst),str_lst)



a = ['Geeks', 'for', 'Geeks']
res = ' '.join(a)
print(type(res),res)

a = ['Geeks', 'for', 'Geeks']

# Convert list to string using a loop
res = ''
for s in a:
    res += s + ' '

# Remove trailing space
res = res.strip()
print(res)
