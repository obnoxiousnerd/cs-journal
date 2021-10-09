# Create a binary file with the name and roll number.
# Search for a given roll number and display the name,
# if not found display the appropriate message.

import pickle


def create_data_file(fd):
    data = []
    n = int(input("Enter number of students: "))
    for _ in range(n):
        print()
        name = input("Enter student name: ")
        roll_no = int(input("Enter student roll no: "))
        data.append({"Name": name, "RollNo": roll_no})
    pickle.dump(data, fd)
    print("Saved data")


def search_name(data, roll_no):
    for entry in data:
        if entry["RollNo"] == roll_no:
            print(f"The name is: {entry['Name']}")
            return
    print(f"No entry found for roll number {roll_no}")


print(
    """
1. Create file
2. Search by roll number
3. Quit
"""
)

while True:
    print()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_data_file(open("rollno_name.dat", "wb"))
    elif choice == 2:
        with open("rollno_name.dat", "rb") as file:
            data = pickle.load(file)
        roll_no = int(input("Enter roll number to search: "))
        search_name(data, roll_no)
    elif choice == 3:
        break
    else:
        print("Invalid choice")
