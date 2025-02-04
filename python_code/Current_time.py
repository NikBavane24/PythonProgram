

import datetime

# using now() to get current time
current_time = datetime.datetime.now()

# Printing value of now.
print("Time now :", current_time)

yesterday = current_time - datetime.timedelta(1)
print("Yesterday time :",yesterday)

# Get Tomorrow
tomorrow = current_time + datetime.timedelta(1)
print("Tomorrow time :",tomorrow)


x = datetime.datetime.now()

print(x.strftime("%a %b %d %Y"))