# The turtle capstone project
import random
import time
from turtle import Turtle, Screen
# ----------------------------------------------------------------
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280

COLORS = ["red", "green", "orange", "blue", "purple", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

FONT = ("Courier", 24, "normal")
# ----------------------------------------------------------------

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)


    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POSITION)

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:

            new_car = Turtle("square")
            new_car.shapesize(stretch_wid= 1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on == True:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect crossing
    if player.is_at_finish_line() == True:
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()




screen.exitonclick()
