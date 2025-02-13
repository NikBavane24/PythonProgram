import sys

a = [("name", "Alice"), ("age", 25), ("city", "New York")]

Dic=dict(a)
print(Dic)

print(str(sys.getsizeof(a)) + " bytes")

test_tup = (5, 20, 3, 7, 6, 8)

test_tup=list(sorted(test_tup))
print(test_tup)