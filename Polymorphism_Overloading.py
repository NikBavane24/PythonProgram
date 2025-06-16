
def product(a, b):
    p = a * b
    print(p)



def product(a, b=0, c=0):
    p = a * b*c
    print(p)

product(4, 5, 5)
product(4)
product(4,5)