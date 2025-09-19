#!/usr/bin/python3
import math

# coordinates of the first point
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# coordinates of the second point
c = int(input("Enter c: "))
d = int(input("Enter d: "))

#formula for the distance 
distance = math.sqrt(((b-a)**2)+((d-c)**2))

# Output the result
print("The distance between the two points is:",distance  )

