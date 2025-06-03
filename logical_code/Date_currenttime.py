from datetime import datetime
import time

current_date=datetime.now()
print(current_date)
print(current_date.strftime("%d %a %b %Y"))

t=time.localtime()
print(t)
