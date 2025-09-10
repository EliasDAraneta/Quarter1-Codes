import math
x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))
dist = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)
print("The distance between the two points is:", dist)