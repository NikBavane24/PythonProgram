

def addNumbers(num1,num2):
    try:
        return  (num1+num2)
    except TypeError:
       return ("Invalid Number")
    except NameError:
        return ("Invalid Parameter")
    #except Exception as e:
        #return (e)


print(addNumbers(10,20))
print(addNumbers(15,"a"))
print(addNumbers(20,30))
print("Exception Handeled")