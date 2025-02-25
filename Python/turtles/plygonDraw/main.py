from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
screen = Screen()
timmy.color("DarkSeaGreen")
screen.colormode(255)

def draw_shape(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        timmy.right(angle)
        timmy.forward(100)

def color_set():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return timmy.pencolor((r, g, b))

for sides in range(3, 11):
    color_set()
    draw_shape(sides)

screen.exitonclick()
