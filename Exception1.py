

def sub(a,b):
    try:
        if (isinstance(a,int)) or (isinstance(a,float)) and (isinstance(b,int)) or (isinstance(b,float)):
            return a-b

        else:
            raise Exception ("Only int and float value allowed")

    except Exception as e:
        return e

print(sub(20,10))
print(sub("a","b"))
print(sub("a",10))
print(sub(10,"b"))