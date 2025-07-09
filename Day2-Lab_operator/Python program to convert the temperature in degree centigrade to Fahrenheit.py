# Program to convert temperature from Celsius to Fahrenheit
degree_symbol = chr(176)
# input temperature in Celsius
celsius = float(input("Enter the temperature in celsius: "))

# convert to Fahrenheit
fahrenheit = (celsius*9/5) + 32

# Display the result
print(f"The temperature in fahrenheit: {fahrenheit:.2f}{degree_symbol}F")
