#TASK -->write a program that calculates the average student height from a List of heights, do not use len and sum function
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# total_height = 0
# for height in student_heights:
#     total_height = total_height + height
# number_of_student = 0
# for student in student_heights:
#     number_of_student = number_of_student + 1
# final_result = round(total_height/number_of_student)
# print(final_result)
#  write a program that calculates the highest score from a List of scores

# student_scores = input("Input a list of student scores ").split()
#
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# max = 0
#
# for x in student_scores:
#     if x > max:
#         max = x
# print(f" The highest score in the class is: {max}")
#sum of even number
# sum = 0
# for even in range(0,101, 2):
#     sum = sum + even
# print(f"result is {sum}")
#TASK FIZZ BUZZ EXERCISE
# for num in range(1,101):
#     if num%5 == 0 and num%3 == 0:
#         print("FizzBuzz")
#     elif num%5 == 0:
#         print("Buzz")
#     elif num%3 == 0:
#         print("Fizz")
#     else:
#         print(num)
#TASK Project password generator
import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print("Welcome to the PyPassword Generator!")
# user_letter = int(input("How many letters would you like in your password ?\n"))
# user_symbol = int(input("How many Symbols would you like ?\n"))
# user_number = int(input("How many Numbers would you like ?\n"))
#Easy level -tip 1 where positon is fixed
# password =""
# pass1 = ""
# pass2 = ""
# for char in range(1, user_letter +1 ):
#     random_char = random.choice(letters)
#     password = password + random_char
#
# for num in range(1, user_number +1 ):
#     random_num = random.choice(numbers)
#     pass1 = pass1 + random_num
#
# for sym in range(1, user_symbol + 1 ):
#     random_sym = random.choice(symbols)
#     pass2 = pass2 + random_sym
# print(password + pass1 + pass2 )
# print(f"{password}{pass1}{pass2}")
#Hard level
# password_list= []
# for char in range(1, user_letter +1 ):
#     password_list = password_list + list(random.choice(letters))
#
# for char in range(1, user_number +1 ):
#     password_list = password_list + list(random.choice(numbers))
#
# for char in range(1, user_symbol + 1 ):
#     password_list = password_list + list(random.choice(symbols))
# print(f" old password is {password_list}")
# random.shuffle(password_list)
# print(f" New password is {password_list}")
#suffling list again and again
# new = []
# for x in range(1,len(password_list) + 1 ):
#     new += list(random.choice(password_list))
# print(f"new password is {new}")
#-----------------------------------------

# my = ['a','b','c','d','e']
# a = [3,2,0,1,4]
# b =[]
# for i  in a:
#     b = b + list(my[i])
# print(b)

# ways of shuffling the code with the for loop.



