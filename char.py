
class Character:

    def method(self):
        a="listen"
        b="silent"
        print("".join(sorted(a)))
        print(a,"".join(b))
        if sorted(a)==sorted(b):
            print("String is anagram")
        else:
            print("String is not anagram")

        print(a[0:3])
        print(b[2:])


c=Character()
c.method()