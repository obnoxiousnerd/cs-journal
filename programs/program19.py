# Program to perform various operations on dictionaries
# i) Create dictionary of months of the year
# ii) Print all keys in alphabetical order
# iii) Print all months with 31 days
# iv) Ask user to enter month name and its no of days
# v) Print key-val pairs sorted by number of days

months = {}
n = 12
for i in range(n):
    print()
    name = input("Enter month name: ")
    days = int(input("Enter number of days: "))
    months[name] = days

print(months)

for key in months:
    if months[key] == 31:
        print(f"{key} : {months[key]}")
print()

name = input("Enter month name: ")
if name in months:
    print(f"Number of days in {name} : {months[name]}")
else:
    print(f"Month {name} not found")

print()

rev_items = [(v, k) for k, v in months.items()]
for i in sorted(rev_items):
    print(f"{i[1]} : {i[0]}")