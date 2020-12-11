from datetime import datetime, date, time, timedelta

# dte = datetime.datetime.now()
# dte = datetime.date.today()
# dte = datetime.date(2020,12,22)
# timeStamp = datetime.date.fromtimestamp(1608615543)

# dte = datetime.date.today()
# print(dte.day, '   ', dte.month, '   ', dte.year, '  ')
#
# t1 = timedelta(weeks=1)
# t2 = timedelta(days=8)
#
# t3 = t1 - t2
#
# print(t2.total_seconds())

# Sử dụng strftime() chuyển đổi datetime sang string

# t1 = datetime.now()
# t2 = '22/12/1996'
# strDte = datetime.strptime(t2, '%d/%m/%Y')
# print((strDte))

#Modulte time
import time
# current_time = time.localtime()
# cr = time.strftime("%d/%m/%Y", current_time)
# print(cr)

# second = time.time()
# cr = time.ctime(second)
# print(cr)

# time_start = time.ctime()
# print(time_start)
#
# time.sleep(10)
#
# time_end = time.ctime()
# print(time_end)

second = time.localtime(86399)
print(second)
