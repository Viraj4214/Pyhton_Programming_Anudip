# Python program to find the largest among three numbers

# Taking input from user
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))

# compare the numbers using if-elif-else

if (number1 >= number2) and (number1 >= number3):
    largest = number1
elif (number2 >= number1) and (number2 >= number3):
    largest = number2
else:
    largest = number3
#display the result
print(f"The largest number is ",largest)
