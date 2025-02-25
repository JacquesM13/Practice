# import colorgram
from turtle import Turtle, Screen
import random
timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.penup()
#
# rgb_colors = []
#
# colors = colorgram.extract("image.jpg", 6)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

# color_list = [(86, 108, 98), (15, 32, 37), (140, 154, 140), (24, 54, 45), (161, 155, 136), (69, 69, 69), (123, 234, 176)]

colors = ['#95918E', '#AF9699', '#80C7C9', '#8EBBD2', '#E3D1C3', '#B3DDEB', '#F3E8CC']

timmy.sety(-240)
timmy.speed("fastest")
timmy.hideturtle()

def up_row():
    timmy.left(90)
    timmy.fd(50)
    timmy.right(90)

for i in range(10):
    timmy.setx(-240)
    for j in range(10):
        timmy.dot(20, random.choice(colors))
        timmy.fd(50)
    up_row()

screen.exitonclick()
