# Program to calculate SI and CI

P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest per annum: "))
T = int(input("Enter rate of interest, in years: "))

SI = P * R * T / 100

A = P * (1 + (R / 100)) ** T
CI = A - P

print(f"SI : {SI}")
print(f"CI(compounded yearly): {round(CI, 3)}")