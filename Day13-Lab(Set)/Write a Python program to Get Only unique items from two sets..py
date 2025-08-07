#Python program to Get Only unique items from two sets.
#input the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

#get unique items
unique_items = set1.union(set2)

#print the result
print("Unique items from two sets: ",unique_items)
