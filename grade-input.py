# GRADE CLASSIFIER PROGRAM
# RUBAIT SIR'S HW: Example: 3

grade = int(input("Enter your grade: "))
if grade > 100:
    print("Invalid Input!")
elif grade >= 90:
    print("Your grade is A")
elif grade >= 80:
    print("Your grade is B")
elif grade >= 60:
    print("Your grade is c")
elif grade < 60:
    print("YOU FAILED!")
else:
    print("Invalid Input!")
