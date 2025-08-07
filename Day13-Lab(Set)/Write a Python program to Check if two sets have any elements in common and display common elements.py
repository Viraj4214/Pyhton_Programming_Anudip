#Python program to Check if two sets have any elements in common. If yes, display the common elements.

#input the sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

#check the common elements
common_elements = set1 & set2

#check and print the result
if common_elements:
    print("Common elements: ",common_elements)
else:
    print("No common elements found")


