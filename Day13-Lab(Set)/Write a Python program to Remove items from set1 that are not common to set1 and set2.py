#Write a Python program to Remove items from set1 that are not common to both set1 and set2

#input the values
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

#Keep only common elements in set1
set1.intersection_update(set2)

#print the reslut
print("Upadated set1 with common elements: ",set1)
