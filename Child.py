from OopsDemo import Cal


class Child(Cal):
    d=200
    def getvalue2(self):
        return self.d + self.a + self.sum()

obj=Child(10,20)
print("******************************")
print(obj.getvalue2())