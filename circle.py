import math

radius = float(input("Enter the radius of a circle:"))

circumference = 2 * math.pi * radius

#print(circumference)
print(f"The circumference of the circle is {round(circumference)}")




#area

import math

radius = float (input("Enter the radius of a circle:"))

#area = math.pi * pow(radius,2)
area = math.pi * (radius ** 2)
print(f"The area of circle is {round(area,3)}")