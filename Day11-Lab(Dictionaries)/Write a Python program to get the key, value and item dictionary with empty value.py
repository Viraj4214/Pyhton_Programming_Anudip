#Create the dictionary
input_dict = {1:10,2:20,3:None,4:40,5:None,6:60}

#Remove the items with none values
clean_dict = {}
for key,value in input_dict.items():
    if value is not None:
        clean_dict[key] = value
        
#Print the result
print("Keys: ")
for key in clean_dict.keys():
    print(key)

print("Values: ")
for value in clean_dict.values():
    print(value)

print("Items(Key-Value)pair: ")
for item in clean_dict.items():
    print(item)
