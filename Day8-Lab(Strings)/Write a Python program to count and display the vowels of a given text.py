#take the input from the user
string = input("Enter a string: ")

#define vowels
vowels = "aeiouAEIOU"

#create a list to store found vowels
found_vowels = []

#Loop through each words in string

for char in string:
    if char in vowels:
        found_vowels.append(char)


#Display the vowels and their count
print("Vowels found: ",found_vowels)
print("Total number of vowels: ",len(found_vowels))
