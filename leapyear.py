year = int(input("Enter a Year "))

if (year % 400 == 0) and (year % 100 == 0):
    print("It is a leap year".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
    print("It is leap year".format(year))
else :
    print("Its not a leap year".format(year))
    