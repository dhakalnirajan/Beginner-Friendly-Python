# Program To Check Whether the User-given Year is a Leap Year or Not.

# Understanding the Program Before Beginning Code.

# Algorithm:
# 1. Ask the user to input a  year in 4-digit integer format.
# 2. Check the condition if year is exactly divisible by 4 and 100, or the year is exactly divisible by 400.
# 3. If the above condition returns true, given year is leap year else it is not leap year.

year = int(input("Enter the year: "))
# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
# ' % ' means modulus or Remainder in the division. in the division 4 divided by 2, the remainder is 0, which is 4 modulus 2.
    print("{0} is a leap year".format(year))
# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))