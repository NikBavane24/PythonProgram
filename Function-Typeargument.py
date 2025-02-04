
#Required arguments
def Subtraction(a,b) :
    c=a-b
    print(c)

Subtraction(20,10)

#Keyword argument
def user_info(name,age):
    print("Hello",name,"Your age is :",age)

user_info("Nikhil",32)
user_info(age=32,name="Nikhil")

#default argument
def user_info_default(name,age=10):
    print("Hello",name,"Your age is :",age)

user_info_default("Nikhil")
user_info_default("Nikhil", 20)

#variable length arguments
def greet(*name):
    for s in name:
        print("Hello",s)

greet("Python")
greet("Java","C++","Ruby")

