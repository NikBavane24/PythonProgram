class Cal:
    a=100
    def __init__(self,b,c):
        self.first=b
        self.second=c
        print("Automatically called")
    def getvalue(self):
        print("Working on python Oops concept")

    def sum(self):
        return self.first + self.second + Cal.a

o=Cal(10,20)
o.getvalue()
print(o.sum())

print("*************************************************")

o1=Cal(50,30)
print(o1.sum())