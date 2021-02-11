# Program to find areas and perimeters of a
# triangle, rectangle and circle

print("For triangle: ")
th = float(input("Enter triangle's height: "))
tb = float(input("Enter triangle's base: "))
ta = 0.5 * tb * th
tp = th + tb + (th ** 2 + tb ** 2) ** 0.5

print("For rectangle: ")
rl = float(input("Enter rectangle's length: "))
rb = float(input("Enter rectangle's breadth: "))
ra = rl * rb
rp = 2 * (rl + rb)

print("For circle: ")
cr = float(input("Enter circle's radius: "))
ca = 3.1416 * (cr ** 2)
cp = 2 * 3.1416 * cr

print(f"Area of triangle: {ta}")
print(f"Area of rectangle: {ta}")
print(f"Area of circle: {ca}")
print(f"Perimeter of triangle: {tp}")
print(f"Perimeter of rectangle: {rp}")
print(f"Perimeter of circle: {cp}")