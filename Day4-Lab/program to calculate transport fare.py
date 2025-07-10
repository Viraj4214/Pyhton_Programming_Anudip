# Python program to calculate transport charges

#take the input from user
distance = float(input("Enter the total distance travelled: "))

#initialize fare charges to zero
charges = 0

#calculate fare charges based on distance travelled

if distance >= 1 and distance <=50:
    charges = distance * 8
elif distance >= 51 and distance <=100:
    charges = 50 * 8 + (distance - 50) * 10
elif distance > 100:
    charges = 50*8 + 50*10 + (distance-100) * 8
else:
    print("Inavild distance")


#display the net fare charges
print(f"The total fare charges for {distance} is: Rs",charges)
