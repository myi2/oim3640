# Exercise 01 - Part 1: Check Fermat's Last Theorem
def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")

def prompt_and_check_fermat():
    a = int(input("Enter a positive integer for a: "))
    b = int(input("Enter a positive integer for b: "))
    c = int(input("Enter a positive integer for c: "))
    n = int(input("Enter a positive integer for n: "))
    check_fermat(a, b, c, n)

# Exercise 01 - Part 2: BMI Calculator
def calculate_bmi(weight, height):
    return weight / (height**2)

def get_bmi_category(weight, height):
    bmi = calculate_bmi(weight, height)
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Exercise 02 - 1: Factorial Program
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Exercise 02 - 2: Fibonacci Program
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Exercise 02 - 3: Greatest Common Divisor Program
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Exercise 02 - 4: Tower of Hanoi
def move(n, source, bridge, destination):
    if n == 1:
        print(f"{source} --> {destination}")
    else:
        move(n-1, source, destination, bridge)
        print(f"{source} --> {destination}")
        move(n-1, bridge, source, destination)

# Example usage of some functions (for those requiring user input, you can call them as needed)
print("BMI Calculator Example:")
bmi = calculate_bmi(70, 1.75)
print(f"BMI: {bmi}, Category: {get_bmi_category(70, 1.75)}")

print("\nFactorial of 5:", factorial(5))
print("Fibonacci number at position 5:", fibonacci(5))
print("GCD of 17 and 12:", gcd(17, 12))

print("\nTower of Hanoi (3 disks):")
move(3, 'A', 'B', 'C')
