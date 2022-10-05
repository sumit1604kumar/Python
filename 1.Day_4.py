#randomisation
#TASK virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
import random
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# result = random.randint(0,1)
# if result == 1:
#     print("Heads")
# else:
#     print("Tails")
#TASK select a random name from a list of names, person selected will pay bill.
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(",")
#
#
# bill = len(names)
# result = random.randint(0, bill -1 )
# print(f"{names[result]} is going to buy the meal today!")
#-----------------------------------------
# a= ['a','b','c','d']
# b=['e','f','g','h']
# c= [a,b]
# print(c[1][1])
#-------------------------------------------------------
# #chase game
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️  ","️⬜️"]
# row3 = ["⬜️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# colum = int(position[0])
# row = int(position[1])
# map[row-1][colum-1] = "X"
# print(f"{row1}\n{row2}\n{row3}")
#-------------------------------------------------------
# value =
# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = [7,8,9]
# r = [l1, l2,l3]
# t = r[1]
# print(r)
# print(r[3-1][1-1])
#Rock paper scissors game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose:{computer_choice}")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")


# print(user,computer)
#
# if my_list[0]>comp_list[2]:
#     print("rock won")
# elif my_list[2]>comp_list[1]:
#     print("sc won")
# elif my_list[1]>comp_list[0]:
#     print("paper won")
#
#
#
