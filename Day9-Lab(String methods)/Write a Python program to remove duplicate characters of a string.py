#take the input from the user
string = input("Enter a string: ")

#split into words
words = string.split()

#store unique_words
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

#join them back
new_string = " ".join(unique_words)

#print the result
print("String after removing duplicates: ",new_string)
