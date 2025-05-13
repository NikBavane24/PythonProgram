import self


class Nonstatic_method:

    def method3(self):
        print("Method3")

    def method4(self):
        Nonstatic_method.method3(self)
        print("Method4")

Nonstatic_method.method4(self)