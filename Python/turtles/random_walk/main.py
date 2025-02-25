from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
screen = Screen()
timmy.color("DarkSeaGreen")
screen.colormode(255)
timmy.speed("fastest")
timmy.pensize(10)


def color_set():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return timmy.pencolor((r, g, b))

def rand_direction():
    directions = [0, 90, 180, 270]
    return random.choice(directions)

for i in range(200):
    color_set()
    direction = rand_direction()
    timmy.setheading(direction)
    timmy.forward(20)

screen.exitonclick()
