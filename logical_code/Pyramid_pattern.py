

rows=int(input("Number of rows for pyramid="))

for i in range(rows):
    for j in range (i+1):
        print("* ",end="")
    print()