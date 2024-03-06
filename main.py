import turtle
import math

pen = turtle.Turtle()
pen.color("red")
pen.speed(0.5)  # Fastest drawing speed
turtle.Screen().bgcolor("black")
screen = turtle.Screen()
screen.screensize(canvwidth=300, canvheight=300)

# Turn off the screen updates
screen.tracer(0.5)


def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)


def heart(x, y):
    pen.fillcolor("black")
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("red")
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
    pen.right(140)  # Reset orientation to default


def txt(x, y):
    pen.penup()
    pen.goto(x - 68, y + 95)
    pen.pendown()
    pen.color("red")  # Changed color for visibility
    pen.write("Nobody 🤣🤣", font=("nunito", 18, "bold"))


# Parameters for the circular pattern
num_hearts = 10  # Total number of hearts to draw
radius = 200  # Radius of the circle

for i in range(num_hearts):
    angle = 360 / num_hearts * i
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))

    # Draw heart and text at calculated position
    heart(x, y)
    txt(x, y)
    pen.setheading(0)  # Reset the turtle's orientation

pen.hideturtle()

# Update the screen after drawing is complete
screen.update()

screen.mainloop()
