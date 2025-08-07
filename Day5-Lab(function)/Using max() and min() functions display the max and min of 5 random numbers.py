#initialize number list
numbers = []
print("Enter five numbers: ")
#taking 5 numnbers from the user using a loop
for i in range(5):
    input_number = int(input(f"Enter number {i+1}: ",))
    numbers.append(input_number)


#display the input numbers
print("The five numbers are: ",numbers)

#display the maximun and minimum numbers
print("The maximum number: ",max(numbers))
print("The minimum number: ",min(numbers))
