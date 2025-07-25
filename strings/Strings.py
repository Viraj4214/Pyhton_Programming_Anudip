# Accepting a string from user
user_string = input("Enter a string: ")

#  Accessing Individual Characters
print("\n First character:", user_string[0])
print("Last character:", user_string[-1])

#  Slicing
print("\n Slicing (0:5):", user_string[0:5])
print("Slicing with negative index (-5:):", user_string[-5:])

#  String Length
print("\nLength of string:", len(user_string))

#  Iterating Over Characters
print("\nCharacters in string:")
for char in user_string:
    print(char, end=' ')
print()

#  Concatenation
another_string = input("\nEnter another string to concatenate: ")
concatenated = user_string + " " + another_string
print(" Concatenation (+):", concatenated)

#  Repetition
print("\n Repetition (*):", user_string * 2)

#  Membership
print("\n Membership Operators:")
check1 = "a" in user_string
check2 = "z" not in user_string
print("'a' in string:", check1)
print("'z' not in string:", check2)

# String Comparison
another_string = input("\nEnter another string for comparison: ")
print("String Comparison:")
if user_string == another_string:
    print("Both strings are equal.")
elif user_string > another_string:
    print(f"'{user_string}' is greater than '{another_string}'")
else:
    print(f"'{user_string}' is less than '{another_string}'")

#  Traversing a String with Index
print("\n Traversing using index:")
for i in range(len(user_string)):
    print(f"Index {i}: {user_string[i]}")

# formatting using .format()
city = input("Enter your name: ")
language = input("Enter your favorite programming language: ")
print("You name is  {} and you love {} programming.".format(city, language))
