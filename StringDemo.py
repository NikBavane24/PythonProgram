str="Shaurya Bavane"
str1="is good boy"
str2="Shaurya1"
str3="  Great  "

print(str[8])             #B
print(str[0:7])           #Shaurya

print(str+" "+str1)       #concatenation = Shaurya Bavane is good boy
print(str2 in str)        #false
var=str.split(" ")
print(var[0])
print(str3.split())
print(str3.lstrip())
print(str3.rstrip())