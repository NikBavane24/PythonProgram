class Person:
    def __init__(self, name,age):
        self.name = name        # Public
        self.age = age
        self._address = "Hidden"  # Protected (convention)
        self.__salary = 5000    # Private

    def display_info(self):
        print(f"Name: {self.name},Age:{self.age}, Salary: {self.__salary}")
p = Person("Alice", 30)
print(p.name)           # ✅ Public: OK
print(p.age)            # ✅ Public: OK
print(p._address)       # ⚠️ Protected: Possible, but discouraged
#print(p.__salary)     # ❌ Error: private attribute
print(p._Person__salary)  # ✅ Works using name mangling
