print("Nguyễn Văn Hùng")
print("2455752021610031")
import datetime as dt
format = "%Y-%m-%dT%H:%M:%S"
t1 = dt.datetime.strptime("2006-12-26T13:02:55", format)
print("Day:", t1.day)
print("Month:", t1.month)
print("Year:", t1.year)
print("Hour:", t1.hour)
print("Minute:", t1.minute)
print("Second:", t1.second)
t2 = dt.datetime.now()
khoang_cach = t2 - t1
print("Số ngày cách xa:", khoang_cach.days)
