#take the input from the user
string = input("Enter the string(with \\n): ")

#remove new lines
clean_string = string.replace("\\n","")

#print the result

print("Cleaned String : ",clean_string)
