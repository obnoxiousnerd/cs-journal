# Program to create a library in Python and import it in a program.

from shape.rect import Rectangle
from shape.sq import Square
from shape.tri import Triangle

rectangle = Rectangle()
square = Square()
triangle = Triangle()

r_area = rectangle.area(10, 20)
s_area = square.area(10)
t_area = triangle.area(10, 20)

print(f"Area of rectangle: {r_area}")
print(f"Area of square: {s_area}")
print(f"Area of triangle: {t_area}")
