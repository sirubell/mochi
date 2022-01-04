import datetime
s = input()
dt = datetime.datetime.strptime(s, "%Y/%m/%d %H:%M:%S")
print(dt)