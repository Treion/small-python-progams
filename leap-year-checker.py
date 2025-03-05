# LEAP YEAR CHECKER PYTHON PROGRAM
# RUBAIT SIR'S HW: Ex: 5

year = int(input("Enter your year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")
