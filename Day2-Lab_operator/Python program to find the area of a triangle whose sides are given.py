#python program to find the area of a triangle whose sides are given

import math

#input the sides of the triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

#calculate semi-perimeter

s = (a+b+c)/2

#calculate area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

#dispaly the result
print(f"The area of the triangle: {area:.2f} square units")



