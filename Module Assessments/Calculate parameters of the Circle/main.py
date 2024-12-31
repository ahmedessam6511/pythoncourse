import math
radius = float(input("Please enter the radius of the circle: "))
if(radius > 0):
    area = math.pi * (radius**2)
    circumference = 2 * math.pi * radius
    print(f"Area equal {area} \n Circumference equal {circumference}")
else:
    print("Please enter a positive number!")