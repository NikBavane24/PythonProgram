import json

s = '["Geeks", "for", "Geeks"]'
a = json.loads(s)
print(type(a),a)
print(type(s),s)

str_1= "I love my India"
b=str_1.split()
print(b)
print(" ".join(b))