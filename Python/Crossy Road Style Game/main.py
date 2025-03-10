import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.colormode(255)
screen.bgcolor((217,217,214))
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

player = Player()

score = Scoreboard()

car = CarManager()

game_is_on = True

screen.onkey(player.forwards, "Up")
screen.onkey(player.backwards, "Down")

while game_is_on:
    time.sleep(0.05)
    screen.update()

    car.create_car()

    car.drive()

    # If player makes it to the other side
    if player.ycor() > 290:
        score.update_score()
        player.refresh()
        car.level_up()

    # Detect collision with car
    for carr in car.cars:
        if carr.distance(player) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()