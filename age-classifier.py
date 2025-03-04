# AGE CLASSIFIER PYTHON PROGRAM
# RUBAIT SIR'S HW: Example: 4

age = int(input("Enter your age: "))
if age >= 65:
    print("You are a senior")
elif age >= 20:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
elif age < 13:
    print("You are a child")
else:
    print("Invalid Input")