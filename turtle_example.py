# modified from https://github.com/spyder-ide/spyder/wiki/How-to-run-turtle-scripts-within-Spyder

# Turtle is a Python module for creating pictures/shapes using a 
# virtual canvas

import turtle

window=turtle.Screen()
window.bgcolor("lightgreen")


# create the turtle, named 'ben', and set attributes
ben = turtle.Turtle() 
ben.color("hotpink")
ben.pensize(5)

# Make ben draw equilateral triangle
ben.forward(80)  # move forward 80 pixels in current direction
ben.left(120)    # turn 120 degrees to the left
ben.forward(80)  # move forward 80 pixels in current direction
ben.left(120)    # turn 120 degrees to the left
ben.forward(80)  # move forward 80 pixels in current direction
ben.left(120)    # turn 120 degrees to the left


#
turtle.done()
turtle.bye()   
