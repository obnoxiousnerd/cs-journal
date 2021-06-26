# To calculate total percentage of marks

print("Enter all the marks out of 50")

eng_marks = int(input("Enter your marks for English: "))
phy_marks = int(input("Enter your marks for Physics: "))
che_marks = int(input("Enter your marks for Chemistry: "))
math_marks = int(input("Enter your marks for Math: "))
cs_marks = int(input("Enter your marks for CS: "))

per = (eng_marks + phy_marks + che_marks + math_marks + cs_marks) * 100 / 250
print(f"Percentage obtained: {per}")