#Python program to Return a set of elements present in Set A or B, but not both.
#input the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

#Get elements present in set1 or set2, but not both
result = set1 ^ set2

#print the result
print("Elements present in set1 or set2, but not both: ",result)
