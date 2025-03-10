from turtle import Turtle

STARTING_POSITION = (0, -285)
MOVE_DISTANCE = 40
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.turtlesize(stretch_len= 1.5, stretch_wid= 1.5)
        self.refresh()

    def forwards(self):
        self.forward(MOVE_DISTANCE)

    def backwards(self):
        self.backward(MOVE_DISTANCE)

    def refresh(self):
        self.goto(STARTING_POSITION)