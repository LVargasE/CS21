# First Turtle Program

# This imports the Turtle Library
import turtle

# Creates a graphics window with light blue background
tableau = turtle.Screen()
tableau.bgcolor("lightblue")

# Create a turtle named donatello (dtello)
dtello = turtle.Turtle()
# Make Donatello red
dtello.color("red")
# Set pen width
dtello.pensize(5)

# Drawing
# Tell donatello to move forward by 150 units
dtello.forward(150)
# Turn left 90 degrees
dtello.left(90)
# Forward march!
dtello.forward(75)
# Turn left 90 degrees
dtello.left(90)
# Forward march!
dtello.forward(150)
# Turn left 90 degrees
dtello.left(90)
# Forward march!
dtello.forward(75)

# Exit and clear screen after user clicks
tableau.exitonclick()
