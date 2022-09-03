import calendar
import sys

year = int(input("Enter a year of your choice: "))

if year == 0000:
    print("Really come on.")
    sys.exit()

month = int(input("Enter a month of your choice: "))

if month == 0:
    print("There is no month such as 0.")
    sys.exit()

elif month > 12:
    print("There is no month great then 12.")
    sys.exit()




print(calendar.month(year, month))