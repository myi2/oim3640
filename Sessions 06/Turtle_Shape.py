import turtle
import math


# Exercise 01
# Drawing a Square
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

leo = turtle.Turtle()
square(leo)
turtle.mainloop()

=====================
# Exercise 02
=====================
# Modify Square with Length Parameter
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

leo = turtle.Turtle()
square(leo, 100)
turtle.mainloop()

#  Polygon Function
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

leo = turtle.Turtle()
polygon(leo, 7, 70)  
turtle.mainloop()

# Circle
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1  
    length = circumference / n 
    polygon(t, n, length)  

leo = turtle.Turtle()
circle(leo, 50)  
turtle.mainloop()

# Arc Function
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

leo = turtle.Turtle()
arc(leo, 50, 180)
turtle.mainloop()   

====================
# Exercise 03
====================
# Drawing 60 Squares, Turning Right 5 Degrees After Each
def draw_spiral_squares(t, number_of_squares=60, turn_angle=5):
    for i in range(number_of_squares):
        square(t, 100)
        t.right(turn_angle)

def square(t, length=100):
    for _ in range(4):
        t.fd(length)
        t.lt(90)

leo = turtle.Turtle()
draw_spiral_squares(leo)
turtle.mainloop()

# Drawing 60 Squares, Each Successively Larger
def draw_growing_squares(t, start_length=30, increment=4, number_of_squares=60, turn_angle=5):
    length = start_length
    for _ in range(number_of_squares):
        square(t, length)
        t.right(turn_angle)
        length += increment

def square(t, length):
    for _ in range(4):
        t.fd(length)
        t.lt(90)

leo = turtle.Turtle()
draw_growing_squares(leo)
turtle.mainloop()

# Drawing Archimedean Spiral
def draw_archimedean_spiral(t, start_radius=10, end_radius=100, angle_increment=5):
    angle = 0
    while start_radius < end_radius:
        t.fd(start_radius)
        t.lt(angle_increment)
        angle += angle_increment
        start_radius += 0.1

leo = turtle.Turtle()
draw_archimedean_spiral(leo)
turtle.mainloop()

