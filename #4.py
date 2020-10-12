day = int(input("Enter the day of the month:"))
month = int(input("Enter the month in numeric form:"))
year = int(input("Enter the last two digits of the year:"))
day_times_month = day * month
if day_times_month == year:
    print("/n This date is magic")
else:
    print("/n This date is not magic")