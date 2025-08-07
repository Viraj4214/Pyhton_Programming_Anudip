#declare lambda function

check_number = lambda x:(
        "Positive" if x > 0 else
        "Negative" if x < 0 else
        "Zero"
)

#take the input from user
number = int(input("Enter a number: "))
#display the result
print("The number is: ",check_number(number))
