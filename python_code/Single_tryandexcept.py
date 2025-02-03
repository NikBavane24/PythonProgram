


try:
    a=1/0
    print(a)
except ZeroDivisionError:
    print("Exception occurs")


def Division(x,y):
    try:
        result=x/y
        print("Answer is =",result)

    except ZeroDivisionError:
        print("Sorry You are dividing by zero ")
Division(100,0)