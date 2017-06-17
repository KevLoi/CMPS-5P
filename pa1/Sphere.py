# Kevin Loi
# kloi@ucsc.edu
# pa1
# Finds volume and surface area of sphere

import math

radius = float(input("Enter the radius of the sphere: "))
surfaceArea = 4 * math.pi * math.pow(radius, 2.0)
volume = (4 * math.pi * math.pow(radius, 3.0))/3
print("The volume is: " + str(volume))
print("The surface area is: " + str(surfaceArea))
