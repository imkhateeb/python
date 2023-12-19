from datetime import *

# Date-Time
datetime_1 = datetime(year=2023, month=10, day=20, hour=23, minute=45, second=56)
print(datetime_1)

datetime_2 = datetime.now()
print(datetime_2)

datetime_3 = date.fromtimestamp(10000000000)
print(datetime_3)


# date class
date_1 = date(year=2023, month=11, day=6)
print(date_1)

date_2 = date.today()
print(date_2)


# time class
time_1 = time(hour=22, minute=23, second=24, microsecond=123456)
print(time_1)


# strftime function
date_3 = date.fromtimestamp(100000000)
print(date_3)

date_4 = date_3.strftime("%A, %B, %Y")
print(f"Date 4 : {date_4}")