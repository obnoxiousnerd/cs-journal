# Write a python database connectivity program to insert, delete, update and read records.

from mysql import connector

connection = connector.connect(user="root", password="12345678", host="localhost")

cursor = connection.cursor()


def display_all():
    cursor.execute("select * from student")
    data = cursor.fetchall()
    count = cursor.rowcount
    print(f"Total number of rows retrieved in resultset: {count}")
    for row in data:
        print(row)


def display_one(roll_num):
    cursor.execute(f"select * from student where RollNo = {roll_num}")
    data = cursor.fetchone()
    print(data)


def display_multi(n):
    cursor.execute("select * from student")
    data = cursor.fetchmany(n)
    count = cursor.rowcount
    print(f"Total number of rows retrieved in resultset: {count}")
    for row in data:
        print(row)


def insert_static():
    query = 'insert into student (RollNo, Name, Marks, Section, Project) values ({}, "{}", {}, "{}", "{}")'.format(
        1, "Pranav", 91.8, "A", "Report card generation"
    )
    cursor.execute(query)
    connection.commit()
    print("Record added successfully")
    display_all()


def insert_custom(rollno, name, marks, section, project):
    query = 'insert into student (RollNo, Name, Marks, Section, Project) values ({}, "{}", {}, "{}", "{}")'.format(
        rollno, name, marks, section, project
    )
    cursor.execute(query)
    connection.commit()
    print("Record added successfully")
    display_all()


def delete_record(roll_num):
    query = f"delete from student where RollNo = {roll_num}"
    cursor.execute(query)
    connection.commit()
    print("Record deleted successfully")
    display_all()


def update_record(roll_num, project):
    query = f"update student set project = '{project}' where RollNo = {roll_num}"
    cursor.execute(query)
    connection.commit()
    print("Record updated successfully")
    display_one(roll_num)


cursor.execute("drop database school")
cursor.execute("create database school")
cursor.execute("use school")

query = """create table student (RollNo int,
Name varchar(255),
Marks float(4,2),
Section char(1),
Project varchar(255))
"""
cursor.execute(query)
print("Table created successfully")

cursor.execute("desc student")
print("Table structure:")
for row in cursor:
    print(row)

ans = "y"
while ans == "y":
    print("1. Insert record using static data")
    print("2. Insert record using custom data")
    print("3. Delete record")
    print("4. Update record")
    print("5. Display n records")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_static()
    elif choice == 2:
        ans = "y"
        while ans == "y":
            rollno = int(input("Enter roll number: "))
            name = input("Enter name: ")
            marks = float(input("Enter marks: "))
            section = input("Enter section: ")
            project = input("Enter project: ")
            insert_custom(rollno, name, marks, section, project)
            ans = input("Do you want to insert more records? (y/n): ")
    elif choice == 3:
        roll_num = int(input("Enter roll number: "))
        delete_record(roll_num)
    elif choice == 4:
        roll_num = int(input("Enter roll number of student to edit: "))
        project = input("Enter new project: ")
        update_record(roll_num, project)
    elif choice == 5:
        n = int(input("Enter number of records: "))
        display_multi(n)
    else:
        print("Invalid choice")

    ans = input("Do you want to continue? (y/n): ").lower()
