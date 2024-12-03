#file=open("test1.txt")

try:
    file=open("test1.txt")

#except:
    #print("Failure of try block")

except Exception as e:
    print(e)

finally:
    print("Finally done")