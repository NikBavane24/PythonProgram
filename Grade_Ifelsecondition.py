

Marks=int(input("Marks="))
if Marks>100:
    print("Wrong value Entered")

elif (Marks>=91 and Marks<=100):
    print("Grade A+")

elif Marks>=81 and Marks<=90:
    print("Grade A")

elif Marks>=71 and Marks<=80:
    print("Grade B")

elif Marks>=61 and Marks<=70:
    print("Grade C")

elif Marks>=51 and Marks<=60:
    print("Grade D")

else:
   print("Fail")