

class Emp():
    def __init__(self,id,name):
        self.id=id
        self.name=name
        print("Parent class as Emp")


class company(Emp):
    def __init__(self,id,name,email):
        super().__init__(id,name)
        self.email=email
        print("Child class as company")

c1=company(1,"vku","kkk@vv.com")
