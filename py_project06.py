#To find out whether a year is leap year or not.
year = int(input("enter year: "))
if year % 4 == 0:
    print("yes,", year, "is a leap year.")
else:
    print("no,", year, "is not a leap year.")
