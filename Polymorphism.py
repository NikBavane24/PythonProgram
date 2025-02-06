
class xyz():
    def websites(self):
        print("Javatpoint is a website out of many available on net.")

    def topic(self):
        print("Python is out of many topics about technology on Javatpoint.")

    def type(self):
        print("Javatpoint is an developed website.")

class PQR():
    def websites(self):
        print("Pink villa is a website out of many available on net. .")

    def topic(self):
        print("Celebrities is out of many topics.")

    def type(self):
        print("pink villa is a developing website.")

obj1 = xyz()
obj2 = PQR()
for domain in (obj1, obj2):
    domain.websites()
    domain.topic()
    domain.type()

def add(a, b):
    return a + b

print(add(3, 4))           # Integer addition
print(add("Hello ", "World!"))  # String concatenation