


try:
    a=1/0
    print(a)
except Exception as e:
    print("Exception occurs",e)


def Division(x,y):
    try:
        result=x/y
        print("Answer is =",result)

    except ZeroDivisionError:
        print("Sorry You are dividing by zero ")
Division(100,0)