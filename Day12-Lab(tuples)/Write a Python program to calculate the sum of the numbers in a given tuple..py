#define list of tuples
tuples_list = [(1,2), (3,4), (5,6)]

#calculate the sum of all numbers
total_sum = sum(x+y for x,y in tuples_list)

#display the result
print("Sum of all numbers in tuple list: ",total_sum)
