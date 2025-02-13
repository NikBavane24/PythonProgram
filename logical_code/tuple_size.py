import sys

Tuple1= ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")

print("Size of Tuple :"+ str(sys.getsizeof(Tuple1)))

list1=list(Tuple1)
length=len(list1)
print(length)