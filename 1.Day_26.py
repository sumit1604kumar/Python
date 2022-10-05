# List comprehension
# num_1 = [1,2,3]
# num_2 = [x+1 for x in num_1]  # format in   [new_item for item in List] we are appending to the new list as well.
# print(num_2)
# #------------------------------------------
# name = "sumit"
# name_new = [letter for letter in name]
# print(name_new)
# #--------------------------------------------
# py = [item *2  for item in range(1, 5)]
# print(py)
# #---------------------------------------------
# fruits =["orange", "apple", "red", "blue"]
# new_fruits = [ sam.upper() for sam in fruits if len(sam) < 5 ]
# print(new_fruits)
# # Some Exercise
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# #--------------------------------------------
# 🚨 Do Not Change the code above 👆



#Write your 1 line code 👇 below:
# squared_numbers = [n*n for n in numbers]
#Write your code 👆 above:

# print(squared_numbers)
# -----------------------------------------------
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [ x for x in numbers if x%2 == 0]
# print(result)
# ----------------------------------------------
# To read from the different files and find out the common number from those two.

# with open("file1.txt") as file_1:
#     data_1 = file_1.readlines()
#
# with open("file2.txt") as file_2:
#     data_2 = file_2.readlines()
#
#
# result = [int(x) for x in data_1 if x in data_2]
# print(result)
#-------------------------------------------------
# new_dict = {new_key:new_value for item in list}==> {new_key:new_value for (key,value) in dict.items() if test}
# import random
# students = ["sumit", "anju", "papa", "mummy"]
# my_dict ={item: random.randint(10, 100) for item in students}
#
# passed_student ={item: score for (item, score) in my_dict.items() if score >= 60 }
#
# print(my_dict)
# print(passed_student)
# # Day 26 project

#user_input = input("Enter the word by your choice:")   dict examples
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# result= {word:len(word) for word in sentence.split()}


# print(result)
import pandas
# student_scores = {
#     "student" :["Angels", "James", "Lily"],
#     "score" : [50, 60, 70]
# }
#
# for (key,value) in student_scores.items():
#     print(key)
#
# abc = pandas.DataFrame(student_scores)
# print(abc)
# # loop through rows of a data frame
# for (index, row) in abc.iterrows():
#     print(row.score)

# starting with the NATO Alphabet Project




data = pandas.read_csv("nato_phonetic_alphabet.csv")
phone_dict = {row.letter:row.code for (index, row) in data.iterrows()}

user_input = input("Enter the word of your choice:\n").upper()
empty_list = [phone_dict[x] for x in user_input]

print(empty_list)









