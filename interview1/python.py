import self
import text1


def method(self):

    list=["Nikhil","Bavane",1234567890,"Pune"]
    list.insert(2,"CES")
    print(list)
    count=0
    for i in list:
        a=str(i)
        for char in a:
            if char=="i":
                count+=1
    print("i char repeats=",count)
    #list.remove("1234567890")
method(self)
print(text1)