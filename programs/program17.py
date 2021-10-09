# Create a CSV file by entering user-id and password,
# read and search the password for given userid.

import csv


def get_password_for_id(file, uid):
    reader = csv.reader(file)
    for row in reader:
        if uid == row[0]:
            print(row[1])
            return
    print("Entry not found")


def create_csv_file(file):
    data = []
    HEADER = ["UserID", "Password"]

    data.append(HEADER)

    n = int(input("Enter number of entries: "))
    for _ in range(n):
        print()
        user = input("Enter username: ")
        passwd = input("Enter password: ")
        data.append([user, passwd])

    writer = csv.writer(file)
    writer.writerows(data)


print(
    """
1. Create file
2. Search by userid
3. Quit
"""
)

while True:
    print()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_csv_file(open("userpass.csv", "w"))
    elif choice == 2:
        with open("userpass.csv", "r") as file:
            userid = input("Enter userid to search: ")
            get_password_for_id(file, userid)
    elif choice == 3:
        break
    else:
        print("Invalid choice")
