# cretae dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Creating a new dictionary and update it with all three
result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)

# Print the Output
print("Concatenated Dictionary:", result)
