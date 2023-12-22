from datetime import datetime
import pytz
t=pytz.timezone('Asia/Kolkata')
current=datetime.now(t)
print(current.strftime('%Y-%m-%d %H:%M:%S.%p'))

tz=pytz.timezone('Africa/Cairo')
c=datetime.now(tz)
print(c.strftime('%Y-%m-%d %H:%M:%S.%p'))

tz_A=pytz.timezone('Australia/Sydney')
c_A=datetime.now(tz_A)
print(c_A.strftime('%Y-%m-%d %H:%M:%S.%p'))
