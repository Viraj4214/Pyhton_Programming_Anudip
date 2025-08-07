#take the input from the user
string = input("Enter a string: ")

#split the words
words = string.split()

#reverse the list of words
reversed_words = words[::-1]

#join the reversed words back into a string
reversed_string = " ".join(reversed_words)

#print the result
print("Reveresed string: ",reversed_string)
