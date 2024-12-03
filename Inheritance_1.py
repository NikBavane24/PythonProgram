from OopsDemo1 import A


class child(A):
    a1=200

    def abc(self):
        return self.a + self.a1

o1 = child()
print(o1.abc())