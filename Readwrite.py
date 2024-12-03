file=open("test.txt")
#print(file.read())
#print(file.read(5))

#print(file.readline())
#print(file.readline())
#print(file.readline())

#line=file.readline()
#while line!="":
 #  line=file.readline()
#file.close()

for line in file.readlines():
    print(line)