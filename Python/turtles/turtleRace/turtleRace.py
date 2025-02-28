from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height= 400, width = 500)

is_race_on = False

colours = ["red", "blue", "yellow", "green", "orange", "purple"]
turtle_list = []

def create_turtle(colour):
    new_turtle = Turtle(shape= "turtle")
    new_turtle.color(colour)
    new_turtle.penup()
    turtle_list.append(new_turtle)

def starting_blocks(turtles):
    width = screen.window_width()
    height = screen.window_height()
    y = - (height/2)
    for turtle in turtles:
        turtle.goto(x= -(width/2) + 20, y= y + 60)
        y += 60
        # if len(turtles) % 2 == 0:
        #
        # else:
            # If odd number of turtles, one should be at y = 0

for colour in colours:
    create_turtle(colour)

starting_blocks(turtle_list)

user_bet = screen.textinput(title= "Make your bet.", prompt= "Which turtle will win the race? Enter a colour: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 220:
            print(f"{turtle.pencolor().title()} wins!")
            if turtle.pencolor() == user_bet.lower():
                print("You won! :)")
            else:
                print("You lost :(")
            is_race_on = False
            
screen.exitonclick()
