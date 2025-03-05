from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 22, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.pencolor("white")
        self.increment()

    def increment(self):
        self.clear()
        self.score += 1
        self.write(arg= f"Score: {self.score}", align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.sety(0)
        self.write(arg=f"Game Over", align=ALIGNMENT, font=FONT)