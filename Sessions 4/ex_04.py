# This program will ask for two numbers and then compute their sum, difference, product, quotient, and power

#Inputs
first_number = int(input("Please enter the first number: "))
second_number = int(input("Please enter the second number: "))

# Calculating different operations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

# Check: division by zero
if second_number != 0:
    division = first_number / second_number
else:
    division = "Cannot divide by zero"

power = first_number ** second_number

# Displaying the results
print(f"{first_number} + {second_number} = {addition}")
print(f"{first_number} - {second_number} = {subtraction}")
print(f"{first_number} * {second_number} = {multiplication}")
print(f"{first_number} / {second_number} = {division}")
print(f"{first_number} ^ {second_number} = {power}")