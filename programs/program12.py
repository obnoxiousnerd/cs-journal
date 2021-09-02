# Write a program to perform read and write operation on CSV file.

import csv


def read_data():
    file = open("student.csv", "r")
    data = csv.reader(file)
    for row in data:
        print(row)


def write_data(data):
    file = open("student.csv", "a")
    writer = csv.writer(file)
    writer.writerow(data)


print("1. Read data from CSV")
print("2. Write data to CSV")
print("3. Quit")

while True:
    choice = int(input("Enter your choice: "))
    continue_asking = True

    if choice == 1:
        read_data()
    elif choice == 2:
        while continue_asking:
            print()
            roll_no = input("Enter roll no of student: ")
            name = input("Enter name of student: ")
            stream = input("Enter stream of student: ")
            marks = input("Enter marks of the student: ")
            choice = input("Do you want to continue? If so, then type 'yes': ")
            if choice != "yes":
                continue_asking = False
            write_data([roll_no, name, stream, marks])
    elif choice == 3:
        break
    else:
        print("You've entered a wrong choice!")

# Empty the file to get the same output everytime.
# THIS LINE IS NOT A PART OF THE ORIGINAL PROGRAM.
open("student.csv", "w+").close()
