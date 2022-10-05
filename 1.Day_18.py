import turtle
from turtle import Turtle, Screen  # Turtle class been imported here.

tim = Turtle()  # object created from the Turtle class
# tim.shape("turtle")
# tim.color("blue")
# # for x in range(4): # draw a line and then turn 90"degree towards left
# #
# #     tim.fd(100)
# #     # tim.lt(90)
# #     tim.dot(20)
#     # timmy_the_turtle.fd(100)
# # for y in range(15):  # drawing a dotted line
# #     tim.pendown()
# #     tim.fd(10)
# #     tim.penup()
# #     tim.fd(10)
# for q in range(3): #Triangle drawn
#     tim.fd(100)
#     tim.rt(120)
# tim.color("red")
#
# # square
# for w in range(4):
#     tim.fd(100)
#     tim.rt(90)
# #draw pentagon
# tim.color("green")
# for e in range(5):
#     tim.fd(100)
#     tim.rt(72)
# tim.color("cyan")
# #hexagon
#
# for r in range(6):
#     tim.fd(100)
#     tim.rt(60)
#
# tim.color("brown")
# #heptagon
#
# for z in range(7):
#     tim.fd(100)
#     tim.rt(51.43)
#
# tim.color("dark magenta")
# # Octogon
#
# for u in range(8):
#     tim.fd(100)
#     tim.rt(45)
#
#
# # nonagon
# tim.color("green")
# for u in range(9):
#     tim.fd(100)
#     tim.rt(40)
#
# # decagon
# tim.color("blue")
# for u in range(10):
#     tim.fd(100)
#     tim.rt(36)
import random

# def draw_shapes(num_of_sides):
#     for x in range(num_of_sides):
#         angle = 360/ num_of_sides
#         tim.forward(100)
#         tim.rt(angle)
# variety = ["red", "green", "blue","yellow","purple","pink","brown","lime"]
#
#
#
#
# for shape in range(3,11):
#     tim.color(random.choice(variety))
#     draw_shapes(shape)
# ---------------------------------------------------------------------------
#import random
# direction = [0,90.180,270]
# tim.speed(10)
# tim.width(6)
# turtle.colormode(255)
#
# def colour():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b=  random.randint(0,255)
#     random_colour = (r,g,b)
#     return random_colour
#
# for x in range(100):
#
#     tim.fd(20)
#     tim.setheading(random.choice(direction))
#     tim.color(colour())

#------------------------------------------------------------
# Draw a spirograph
# import random
#
# turtle.colormode(255)
# tim.speed("fastest")
#
# def colour():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b=  random.randint(0,255)
#     random_colour = (r,g,b)
#     return random_colour
#
# def graph(gap):
#     for p in range(int(360/gap)):
#         tim.color(colour())
#         tim.circle(100)
#         tim.setheading(tim.heading() + gap)
#
# graph(5)

#
# import colorgram
# rgb_colours = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r,g,b)
#     rgb_colours.append(new_colour)
#
#
# print(rgb_colours)
import random
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136),
           (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
           (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
           (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()
turtle.colormode(255)
tim.speed("fastest")
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()
