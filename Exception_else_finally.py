


def subtraction(num1,num2):
    try:
        print(num1-num2)
    #except TypeError:
        #print("Invalid Number")
    except Exception as e:
        print(e)

    else:
        print("Calculation completed")

    finally:
        print("Program is completed")


print(subtraction(20,"a"))
