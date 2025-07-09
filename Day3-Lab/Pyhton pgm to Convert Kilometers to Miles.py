# python program to convert kilometers to miles

#take input from the user

kilometers = float(input("Enter the distance in kilometers: "))

#conversion factor
conversion_factor = 0.621371

#Calculate miles

miles = kilometers * conversion_factor

#display the result
print(f"{kilometers} km is equal to {miles:.2f} miles.")

