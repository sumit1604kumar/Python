# More on turtle graphics, Event Listeners, state and multiple instances

# from turtle import Turtle,Screen
# tim = Turtle()
#
# screen = Screen()
#
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def move_counter_clock():
#     tim.left(10)
#
# def move_clock():
#     tim.right(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_counter_clock)
# screen.onkey(key="d", fun=move_clock)
# screen.onkey(key="c", fun=clear)
#
# screen.exitonclick()

# --------------------------------------------------------------------
import turtle
from turtle import  Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="which will win the game? choose your colour:")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-120, -60, 0, 50, 100, 150]
all_turtles =[]




for index in range(0,6):

    new_tim = Turtle(shape="turtle")
    new_tim.color(colors[index])
    new_tim.penup()
    new_tim.goto(x=-230, y=y_position[index])
    all_turtles.append(new_tim)

if user_bet:
    is_race_on = True

while is_race_on == True:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_colour = turtle.pencolor()
            if win_colour == user_bet:
                print(f"User has won the race {win_colour}")
            else:
                print(f"lost the game, winner is {win_colour}")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
