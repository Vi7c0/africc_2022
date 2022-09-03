import calendar
import sys

#getting input to use as a year
year = int(input("Enter a year of your choice: "))

#cheking to see if year is equal to 0000 and then program stops
if year == 0000:
    print("Really come on.")
    sys.exit()

#gets input to use as a month
month = int(input("Enter a month of your choice: "))

#checks to see if month is equal to 0 and then the program stops
if month == 0:
    print("There is no month such as 0.")
    sys.exit()

#checks to see if month input is greater then 12 and then program stops
elif month > 12:
    print("There is no month great then 12.")
    sys.exit()

#outputs calendar
print(calendar.month(year, month))