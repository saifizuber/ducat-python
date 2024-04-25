import datetime

t=datetime.datetime.now()

s=t.time()

d=t.date()


t1=d.strftime('%d/%m/%y')
print(t1)

print(s)
print(d)
print(s.hour,':',s.minute)
print(d.day,'/',d.month,'/',d.year)


t1=d.strftime('%d/%m/%y')# gave date in dd/mm/yy
print(t1)

t1=d.strftime('%A')# print day(like monday, tuesday, wednesday etc.)
print(t1)
t1=d.strftime('%d/%m/%y %A')# print date and day at once
print(t1)

h=s.strftime('%H:%M:%S')# print time's second in the s
print(h)

h=s.strftime('%I:%M:%S %p')# %I will print in 12 hours
print(h)



s=datetime.date(2020,5,15)

h=s.strftime('%d/%m%y %a')
print(h)

h=s.strftime('%d/%B/%y %a') # Capital 'B' print the month in alphabet (may,jun,jul,apr etc.)
print(h)

import calendar

print(calendar.month(2002,9))
print(calendar.prcal(2025)) #prcal means particular canledar
