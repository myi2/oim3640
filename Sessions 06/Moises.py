import turtle
import math

def circle(t, r):
    """Draws a circle with the given radius."""
    circumference = 2 * math.pi * r
    n = 50  # Number of sides in the polygon approximation of the circle
    length = circumference / n  # Length of each side in the polygon
    polygon(t, n, length)

leo = turtle.Turtle()  # Create a turtle named leo
circle(leo, 50)  # Draw a circle with radius 50
turtle.mainloop()  # Start the turtle graphics event loop
