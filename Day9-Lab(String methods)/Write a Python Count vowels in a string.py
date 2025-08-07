#take the input from the user

string = input("Enter a string: ")

#define vowels
vowels = "aeiouAEIOU"

#empty list to store found vowels
found_vowels = []

#loop through each character

for char in string:
    if char in vowels:
        found_vowels.append(char)

#print the result
print("Vowels: ",found_vowels)
print("Total number of vowels: ",len(found_vowels))
        
