#function to divide two numbers

def div(a,b):
    if b!= 0:
        result = a / b
        print("The division is: ",result)
    else:
        print("Error: division by zero is not defined")


#call the function with two numbers
div(10,2)
