# data library Panda

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             content = row[1]
#             temp.append(int(content))
#     print(temp)


import pandas
# dataa = pandas.read_csv("weather_data.csv")
# val = dataa["temp"]
# print(val)
# print(dataa[dataa.day == "Monday"])
# # average_temp = sum(val)/len(val)
# # print(average_temp)
# # print(dataa["temp"].max())
#
# # to get the data from the row
# max_temp = dataa["temp"].max()
# pr_row = dataa[dataa.temp == 24]
# print(pr_row)
# monday = dataa[dataa.day == "Monday"]
# celcius = monday.temp
# result = (celcius *9/5) + 32
# print(result)
# # print(dataa[dataa.day == "Monday"])
#
# # crete a dataframe from scratch
# data_dict= {
#     "students":["Amy", "Sammy", "Pammy"],
#     "scores":[76, 56, 98],
# }
#
# sam_data = pandas.DataFrame(data_dict)
# print(sam_data)
# sam_data.to_csv("my_sumit.csv")

#---------------------------------------------------------------------
# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# grey_squirrel = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
# red_squirrel = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
# print(grey_squirrel, red_squirrel, black_squirrel)
#
# squirrel_dict = {
#     "Fur Colour":["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrel, red_squirrel, black_squirrel],
# }
#
# sq_data = pandas.DataFrame(squirrel_dict)
# sq_data.to_csv("data_derived_squirrel.csv")

# ___---------------------------------------------------------------

# USA MAP PROJECT
import turtle


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)   # adding shape to the Turtle class

turtle.shape(image)

def cordinates(x, y):  #  to get the co-ordinates from the screen.
    print(x,y)
turtle.onscreenclick(cordinates)

guess = []

score = 0
while len(guess) < 50:

    answer_state = screen.textinput(title= f"Score is {score}/50", prompt="What's the another state name ?").title()
    data = pandas.read_csv("50_states.csv")
    all_state = data["state"].to_list()

    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guess:
                missing_state.append(state)
                print(missing_state)
        break


    if answer_state in all_state:
        guess.append(answer_state)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # game_on = False



turtle.mainloop()