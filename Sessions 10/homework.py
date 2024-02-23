# Exercise 01: String Slicing and Immutability Examples
team = 'New England Patriots'
print(team[0:11])  # New England
print(team[12:])   # Patriots
print(team[:])     # New England Patriots

# Exercise 02: Count Function
def count(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count

# Example usage of count function
print(count('New England Patriots', 'a'))  # Outputs: 2

# Exercise 03: String Methods Exploration
team_upper = team.upper()
print(team_upper)  # Outputs: NEW ENGLAND PATRIOTS

# Using split, strip, replace
print(team.split())  # ['New', 'England', 'Patriots']

# Exercise 04: Analyzing Functions for Lowercase Detection
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
    return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return True
    return False

def any_lowercase3(s):
    flag = False
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

# Exercise 05: Caesar Cipher
def rotate_word(s, n):
    result = ''
    for char in s:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            rotated_char = chr((ord(char) - start + n) % 26 + start)
            result += rotated_char
        else:
            result += char
    return result

# Example usage of rotate_word function
print(rotate_word('cheer', 7))  # Outputs: 'jolly'
print(rotate_word('melon', -10))  # Outputs: 'cubed'
print(rotate_word('HAL', -1))  # Outputs: 'GZK'

# Testing any_lowercase functions with a sample string
sample_string = 'Python'
print(any_lowercase1(sample_string))  # Expected: True
print(any_lowercase2(sample_string))  # Misleading, always True due to 'c'
print(any_lowercase3(sample_string))  # Depends on the last character
print(any_lowercase4(sample_string))  # True, correct implementation
print(any_lowercase5(sample_string))  # False, expects all to be lowercase
