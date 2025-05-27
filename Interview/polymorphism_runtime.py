import self


class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog sound as bho bho")

class Cat(Animal):
    def sound(self):
        print("Cat sound as meow meow")

def make_animal_sound(animal):
    animal.sound()

a=Animal()
d=Dog()
c=Cat()

make_animal_sound(a)
make_animal_sound(d)
make_animal_sound(c)

