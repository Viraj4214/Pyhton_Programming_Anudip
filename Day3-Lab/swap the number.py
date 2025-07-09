#program to swap numbers

#take input from the user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

#before swapping
print(f"Before swapping : a = {a}, b = {b}")

#create the temporary variable and swap the number

temp1 = a
a = b
b = temp1

#display the result
print(f"After swapping: a = {a}, b = {b}")

