import math 

def area_circle_fn(radius):
    return math.pi * radius * radius

def perimeter_circle_fn(radius):
    return 2 * math.pi * radius

def diameter_circle_fn(radius):
    return 2 * radius  
      
def calculate_for_circle(radius, fn):
    return fn(radius)

print("Diameter of circle with radius 5 :",calculate_for_circle(10, diameter_circle_fn))

print("Perimeter of cicle with radius of 5 :", calculate_for_circle(10, perimeter_circle_fn))

print("Area of circle with radius of 5 :",calculate_for_circle(10, area_circle_fn))
