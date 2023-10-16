import datetime as d
import calendar as c
#month, day, year
in_date = input().split() # mm dd yyyy format
#and it should be year,month,day
our_date = d.date(int(in_date[2]), int(in_date[0]), int(in_date[1]))
result = c.day_name[our_date.weekday()].upper()
print(result)
