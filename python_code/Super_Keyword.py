

class Parentclass:
    def parent_method(self):
        print("This is the parent method")


class Childclass(Parentclass):
    def parent_method(self):
        print("This is the parent method of child")
    def child_method(self):
        print("This is the child method")

        super().parent_method()


Child_obj=Childclass()

Child_obj.child_method()
Child_obj.parent_method()


