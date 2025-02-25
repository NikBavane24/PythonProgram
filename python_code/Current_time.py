

import datetime

# using now() to get current time
current_time = datetime.datetime.now()

# Printing value of now.
print("Time now :", current_time)

yesterday = current_time - datetime.timedelta(1)
print("Yesterday time :",yesterday)

twodaysbefore= current_time-datetime.timedelta(2)
print("two days before:",twodaysbefore)

# Get Tomorrow
tomorrow = current_time + datetime.timedelta(1)
print("Tomorrow time :",tomorrow)

dayaftertomorrow = current_time + datetime.timedelta(2)
print("day after tomorrow :",dayaftertomorrow)


x = datetime.datetime.now()

print(x.strftime("%a %b %d %Y"))