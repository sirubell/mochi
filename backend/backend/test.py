import datetime

start_time = datetime.datetime(year=2022,month=1,day=2,hour=12,minute=30,second=40)
end_time = datetime.datetime(year=2022,month=1,day=2,hour=18,minute=30,second=50)

h = int(input())
m = int(input())
s = int(input())
now_time = datetime.datetime(year=2022,month=1,day=2,hour=h,minute=m,second=s)

timedelta = end_time-start_time
print(timedelta.total_seconds()//60)
timedelta = now_time-start_time
print(timedelta.total_seconds()//60)
if now_time > start_time and now_time < end_time:
    print("OK")