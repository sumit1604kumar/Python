# TASK 1 odd and Even, I had used modulo as it will give the remainder as the output
# number = int(input("which number do you want to check ? "))
# if number%2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")
#TASK BMI 2.0
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = round(weight/(height ** 2))
# if bmi< 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi> 18.5 and bmi<25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi>25 and bmi<30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi>30 and bmi<35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")
#TASK To find the given year is leap year or not.
# year = int(input("Which year do you want to check? "))
# if year%4 == 0:
#     if year%100 == 0:
#         if year% 400 == 0:
#             print("Leap ear")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")
#TASK PIZZA program
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is ${bill}.")
#TASK 4 program that tests the compatibility between two people.
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# lname1, lname2 = name1.lower() , name2.lower()
#
# sum1 = lname1.count('t') + lname1.count('r') + lname1.count('u') + lname1.count('e') + lname2.count('t') + lname2.count('r') + lname2.count('u') + lname2.count('e')
# sum2 = lname2.count('l') + lname2.count('o') + lname2.count('v') + lname2.count('e') + lname1.count('l') + lname1.count('o') + lname1.count('v') + lname1.count('e')
# score1, score2 = int(sum1), int(sum2)
# love = score2 + score1 * 10
#
# if love < 10:
#     print(f"Your score is {love}, you go together like coke and mentos.")
# elif love > 90:
#     print(f"Your score is {love}, you go together like coke and mentos.")
# elif love > 40 and love < 50:
#     print(f"Your score is {love}, you are alright together.")
# else:
#     print(f"Your score is {love}.")
#TASK final project for the day.

print("Welcome to the Treasure Island, your mission is to find the treasure")
turn = input("select left or right")
# swim = input(" select swim or wait")
# door = input("select the door Red, blue or yellow")

if turn  == "left":
    swim = input(" select swim or wait")
    if swim == "wait":
        door = input("select the door Red, blue or yellow")
        if door == "yellow":
            print("you win")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")








