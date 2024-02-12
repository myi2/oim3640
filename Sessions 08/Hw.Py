# Exercise 01: Calculating Sums

# Calculate the sum of integers from 1 to 10
sum_1_to_10 = sum(range(1, 11))
print(sum_1_to_10)

# Calculate the sum of integers from 1 to 1000
sum_1_to_1000 = sum(range(1, 1001))
print(sum_1_to_1000)

# Calculate the sum of all odd numbers from 1 to 1000
sum_odds_1_to_1000 = sum(range(1, 1001, 2))
print(sum_odds_1_to_1000)

# Calculate the sum of all even numbers from 1 to 1000
sum_evens_1_to_1000 = sum(range(2, 1001, 2))
print(sum_evens_1_to_1000)

# Rewriting with While Loops

# Sum of integers from 1 to 10 using while loop
i = 1
sum_1_to_10_while = 0
while i <= 10:
    sum_1_to_10_while += i
    i += 1
print(sum_1_to_10_while)

# Sum of integers from 1 to 1000 using while loop
i = 1
sum_1_to_1000_while = 0
while i <= 1000:
    sum_1_to_1000_while += i
    i += 1
print(sum_1_to_1000_while)

# Sum of all odd numbers from 1 to 1000 using while loop
i = 1
sum_odds_1_to_1000_while = 0
while i <= 1000:
    if i % 2 == 1:
        sum_odds_1_to_1000_while += i
    i += 1
print(sum_odds_1_to_1000_while)

# Sum of all even numbers from 1 to 1000 using while loop
i = 1
sum_evens_1_to_1000_while = 0
while i <= 1000:
    if i % 2 == 0:
        sum_evens_1_to_1000_while += i
    i += 1
print(sum_evens_1_to_1000_while)

# Exercise 03: Newton's Method for Square Roots

import math

def mysqrt(a):
    x = a / 2  # Initial guess
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < 1e-10:
            break
        x = y
    return x

def test_square_root():
    for a in range(1, 10):
        mysqrt_a = mysqrt(a)
        math_sqrt_a = math.sqrt(a)
        diff = abs(mysqrt_a - math_sqrt_a)
        print(f"{a} {mysqrt_a} {math_sqrt_a} {diff}")

# Call test_square_root to print the comparison table
test_square_root()
