# Program to convert height in cm to other units

h_cm = float(input("Enter height in cm: "))

CM_FACTORS = {
    "MM": 0.01,
    "M": 100,
    "IN": 2.54,
    "FT": 30.48,
}

print(f"Height in metres : {h_cm / CM_FACTORS['M']} m")
print(f"Height in millimetres : {h_cm / CM_FACTORS['MM']} mm")
print(f"Height in inches : {h_cm / CM_FACTORS['IN']} in")
print(f"Height in feet : {h_cm / CM_FACTORS['FT']} ft")