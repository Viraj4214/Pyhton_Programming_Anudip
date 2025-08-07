#take the input from the user
string = input("Enter a string: ")

#initialize counters
letters = 0
digits = 0
special_chars = 0

#Loop through each character
for char in string:
    if char.isalpha():
        letters = letters + 1
    elif char.isdigit():
        digits = digits + 1
    else:
        special_chars = special_chars + 1

#print the result
print("Total letters:", letters)
print("Total digits:", digits)
print("Total special symbols:", special_chars)
