# Empty dictionary to store key-value pairs
test_dict = {}

# Ask the user how many entries you want to add
n = int(input("How many items do you want to enter? "))

# Loop to take input from the user
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = int(input(f"Enter value for {key}: "))
    test_dict[key] = value

# Calculate mean
values = test_dict.values()
mean = sum(values) / len(values)

# Display and print result
print("Your dictionary:", test_dict)
print("Mean of values:", mean)
