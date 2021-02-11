# Get marks of all students and print them in manner
tmarks = list()
n = int(input("Enter number of students: "))
for i in range(n):
    # Newline to avoid verbosity
    print()
    print(f"Student {i+1}")
    m1 = int(input("Enter marks in subject 1: "))
    m2 = int(input("Enter marks in subject 2: "))
    m3 = int(input("Enter marks in subject 3: "))
    marks = (m1, m2, m3)
    tmarks.append(marks)
# Because output form should be in tuple, convert list to tuple
print(tuple(tmarks))