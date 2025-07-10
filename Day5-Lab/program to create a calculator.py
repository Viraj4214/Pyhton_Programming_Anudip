# python program to accept a choice from the user and create a calculator

print("Welcome to the calculator")
print("Choose your operation: ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

# accept choice from the user
choice = input("Enter your choice (1/2/3/4):")

# accept choice from the user
if choice in ['1','2','3','4']:
    #accept the two numbers from tyhe user
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    #perform the operation
    if choice == '1':
        result = number1 + number2
        print(f"Result for addition of {number1} and {number2}:",result)
    elif choice == '2':
        result = number1 - number2
        print(f"Result for subtraction of {number1} and {number2}:",result)
    elif choice == '3':
        result = number1 * number2
        print(f"Result for multiplication of {number1} and {number2}:",result)
    elif choice == '4':
        if number2 != 0:
            result = number1 / number2
            print(f"Result for division of {number1} and {number2}:",result)
        else:
            print("Error: Cannot divide by zero")
else:
    print("Inavlid choice! Please enter 1, 2, 3, 4")
    

