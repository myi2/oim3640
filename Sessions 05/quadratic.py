def quadratic(a, b, c):
    """Solves the quadratic equation ax^2 + bx + c = 0 for real roots and returns the two roots."""
    d = b**2 - 4*a*c
    
    if d < 0:
        return "The equation has complex roots."
    
    root1 = (-b - d**0.5) / (2 * a)
    root2 = (-b + d**0.5) / (2 * a)
    
    return root1, root2

# Example usage
a, b, c = 1, 5, 6
root1, root2 = quadratic(a, b, c)
print(f"The roots of the equation {a}x^2 + {b}x + {c} = 0 are: {root1} and {root2}.")
