# triangle_type.py

# Get user input for the three sides
side1 =int(input("Enter length of side 1: "))
side2 =int(input("Enter length of side 2: "))
side3 =int(input("Enter length of side 3: "))

if side1 == side2 == side3:
        print("The triangle is Equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is Isosceles.")
else:
        print("The triangle is Scalene.")


