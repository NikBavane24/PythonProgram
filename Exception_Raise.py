


def addNumbers(num1,num2):
    try:
        if (isinstance(num1,int)) or (isinstance(num1,float)) and (isinstance(num2,int)) or (isinstance(num2,float)):
            return (num1+num2)
        else:
            raise Exception ("Only Int and Float values are allowed")

    except Exception as e:
        return e


print(addNumbers(10,20))
print(addNumbers("a","b"))


