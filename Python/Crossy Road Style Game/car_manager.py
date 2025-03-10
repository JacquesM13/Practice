from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
LANES = [-240, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240]


class CarManager:
    def __init__(self):
        self.cars = []
        # self.create_car()
        self.move_increment = 10

    def create_car(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            new_car = Turtle(shape= "square")
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(stretch_wid= 1.5, stretch_len= 2.5)
            new_car.penup()
            new_car.goto(x= random.randint(400, 600), y = random.choice(LANES))
            new_car.setheading(180)
            self.cars.append(new_car)

    def destroy_car(self, car):
        self.cars.remove(car)
        car.hideturtle()

    def drive(self):
        for car in self.cars:
            car.forward(self.move_increment)
            if car.xcor() < -400:
                self.destroy_car(car)

    def level_up(self):
        self.move_increment += 1.4


    def position_x(self):
        for car in self.cars:
            return car.xcor()

    def position_y(self):
        for car in self.cars:
            return car.ycor()