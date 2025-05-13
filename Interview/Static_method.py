
class Static_method2:

    @staticmethod
    def method1():
        print("Method1")
    @staticmethod
    def method2():
        Static_method2.method1()
        print("Method2")

Static_method2.method2()