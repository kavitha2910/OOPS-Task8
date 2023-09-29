
1)import math

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_area(self):
        areas = [math.pi * (r ** 2) for r in self.radius_list]
        return areas

radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_list)

areas = circle.calculate_area()
for i, r in enumerate(radius_list):
    print(f"Circle {i+1}:")
    print(f"Radius: {r}")
    print(f"Area: {areas[i]}")
    print()


3)import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def area(cls, radius):
        return math.pi * radius**2

    @classmethod
    def perimeter(cls, radius):
        return 2 * math.pi * radius
radius_values = [10, 501, 22, 37, 100, 999, 87, 351]
for radius in radius_values:
    circle = Circle(radius)
    circle_area = Circle.area(radius)
    circle_perimeter = Circle.perimeter(radius)
    print(f"For radius {radius}:")
    print(f"Area: {circle_area:.2f}")
    print(f"Perimeter: {circle_perimeter:.2f}")
    print()

