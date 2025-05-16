class Father:
    def skills(self):
        print("Father: Gardening, Carpentry")

class Mother:
    def skills(self):
        print("Mother: Cooking, Painting")

class Child(Father, Mother):
    def skills(self):
        print("Child: ", end="")
        Father.skills(self)
        Mother.skills(self)
