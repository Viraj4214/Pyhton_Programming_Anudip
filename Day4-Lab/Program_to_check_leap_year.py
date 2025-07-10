'''
 Program to check leap year
 '''
#take input from user
year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is leap year")
elif (year % 4 == 0) and (year % 100 !=0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
