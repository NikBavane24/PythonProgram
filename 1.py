class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        print("Your name is",name,"age is",age)

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
print(dog1.name)
print(dog1.species)
print(dog1.age)