


num=int(input("Enter the number="))
sum=0

for digit in str(num):
    sum += int(digit)

print(sum)
if sum%3==0:
    print("Number is divisible by 3")

else:
    print("Number is not divisible by 3")