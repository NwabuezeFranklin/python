import datetime
import time
w = datetime.datetime(2022,7,17)
x = datetime.datetime.now()
print("Day:",x.strftime("%A"))
print("Day abbrev:",x.strftime("%a"))
print("Month:",x.strftime("%B"))
print("Month abbrev:",x.strftime("%b"))
print("Week as a number \"0 - 6\":",x.strftime("%w"))
print("Year:",x.strftime("%Y"))
print("Year abbrev:",x.strftime("%y"))
print("Hour 0 - 24:",x.strftime("%H"))
print("Hour 0 - 12:",x.strftime("%I"))
print("Month as a number \"0 - 12\":",x.strftime("%m"))
print("Day of the Month",x.strftime("%d"))
print("am/pm",x.strftime("%p"))
print("Minute",x.strftime("%M"))
print("Second",x.strftime("%S"))
print("Micro Second",x.strftime("%f"))
print("UTC",x.strftime("%z"))
print("Day number of year",x.strftime("%j"))
print("week number of year",x.strftime("%U"))
print("Important Local version date and time",x.strftime("%c"))
print("Local version of date",x.strftime("%x"))
print("Local version of time",x.strftime("%X"))
y = time.strftime("%I:%M:%S%p %m %b",time.gmtime())
print(w)
print(x)
print(y)