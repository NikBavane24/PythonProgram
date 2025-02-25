


num=int(input("Enter the number="))
sum=0

for i in str(num):
    sum += int(i)

print(sum)
if sum%3==0:
    print("Number is divisible by 3")

else:
    print("Number is not divisible by 3")