#3
def my_abs(x):
    """Prints the absolute value of any number without using the built-in abs() function."""
    if x < 0:
        print(-x)
    else:
        print(x)

# Example usage
my_abs(-5)
my_abs(3)

#4
def my_abs(x):
    """Returns the absolute value of any number without using the built-in abs() function."""
    if x < 0:
        return -x
    else:
        return x

# Example usage
result1 = my_abs(-5)
result2 = my_abs(3)
print(result1)
print(result2)

#5
def my_abs(x):
    if isinstance(x, int) or isinstance(x, float):
        if x < 0:
            x = -x
        return x
    else:
        print("Error: The input must be an integer or a float.")
        return None  

# Example usage of the function
print(my_abs(-10))  
print(my_abs(10.5))  
print(my_abs("Hello"))  



