import self


def method(self):

    list=["Nikhil","Bavane","Puneri"]
    list.insert(2,"CES")
    print(list[3],type(list[3]))
    string1=" ".join(list)
    print(string1)
    count=0
    for char in string1:
        if char=="i":
            count+=1
    print(count)


method(self)