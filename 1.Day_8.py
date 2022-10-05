#functions with parameters --> Basic one
# def greet():
#     print("1. This is the first line")
#     print("2. This is the second line")
#     print("3. This is the third line ")
# greet()

#functions with parameters --> with parameter, Variable contains the value 123 in a
# def reet(a):
#     print(f"1. This is the first line{a}")
#     print(f"2. This is the second line{a}")
#     print(f"3. This is the third line {a}")
# reet(123)

# functions with the multiple input --> positional arguments
# def eet(name, location):
#     print(f"My name is {name}")
#     print(f"My location is {location}")
# eet("sumit","Sydney")

# functions with different positional arguements
# def et(name, location):
#     print(f"My name is {name}")
#     print(f"My location is {location}")
# et(location="sumit",name="Sydney")

#TASK 1 Wall paint exercise

# import math
# def paint_calc(height, width, cover):
#     number_of_cans = math.ceil((height * width)/ coverage)
#     print(f"You'll need {number_of_cans} cans of paint")
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

#TASK 2 Prime number checker

# def prime_checker(number):
#     is_prime = True
#     for x in range(2, number):
#         if number%x == 0:
#             is_prime = False
#     if is_prime == True:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number")
#
#
# n = int(input("Check this number: "))
# prime_checker(number=n)

# Project Carser encryption - My Try
# en = input("Type encode or decode !")
#
#
#
#
# def encryption():
#     user_string = input("enter the word\n")
#     word = list(user_string)
#     shift = int(input("enter the shift\n"))
#     print(f"The key used to encrypt is {shift}")
#     alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     print(f" Original word is : {user_string}")
#     num_list = ""
#     for x in range(len(word)):
#         result = word[x]
#         num = alpha.index(result) # for aa num value is 0 here
#         num_shift = num + shift
#         num_list = num_list + alpha[num_shift]
#     print(f" The encryption key is : {num_list}")
#     return num_list
#
#
#
#
# # val = encryption()
#
#
# def decryption(num_list):
#     print(f" We need to decrypt the following : {num_list} ")
#     user_back = int(input("Enter the back shift key"))
#     gamma = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     back_shift = list(num_list)
#     print(back_shift)
#     final_list = ""
#     for y in range(len(back_shift)):
#         d_result = back_shift[y]
#         pos = gamma.index(d_result)
#         back = pos - user_back
#         final_list = final_list + str(gamma[back])
#     print(f"decrypted anser is {final_list}")
#
#
# # decryption(val)
#
# if en == "encode":
#     val = encryption()
#
# elif en == "decode":
#     decryption(val)
# else:
#     print("better luck next time")

# Encry-Decrypt game
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text = end_text +  alphabet[new_position]
        else:
            end_text = end_text + char
    print(f"The {cipher_direction}d text is {end_text} ")

should_continue = True
while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Want to go again type 'Yes' and 'No' !")
    if result == "no":
        should_continue = False
        print("Good Bye, program had ended")