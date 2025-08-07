#take the input from the user
string = input("Enter a string: ")

#initialize counters
uppercase = 0
lowercase = 0
digits = 0
special_chars = 0

#loop through each character in the string
for char in string:
    if char.isupper():
        uppercase = uppercase + 1
    elif char.islower():
        lowercase = lowercase + 1
    elif char.isdigit():
        digits = digits + 1
    else:
        special_chars = special_chars + 1

#print the result
print("Uppercase: ",uppercase)
print("Lowercase: ",lowercase)
print("Digits: ",digits)
print("Special_chars: ",special_chars)
