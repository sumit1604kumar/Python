# #TASK 1
# print("Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python print function")
# print("Day 1 - Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")
# #TASK 2
# print("sumit\nKumar")
# print("Anju" + " "+ "Sumit")
# print("************************************************************")
# print("Day 1 - String Manipulation")
# print('String Concatenation is done with the "+" sign.')
# print('e.g. print("Hello " + "world")')
# print("New lines can be created with a backslash and n.")
# #TASK 3
# # print("Hello" + input("\nenter my name\n"))
# # print(len(input("What is your name?")))
# # TASK 4
# # a = input("a:")
# # b = input("b:")
# #a, b = b, a  # swapping the value between the variables
# # print(a)
# # print(b)
# #Project 1
# print("Welcome to Brand Name Generator")
# city = input("What is the Name your City?\n")
# pet = input("What is the Name of your Pet?\n")
# print("Your Band name could Be " + city + " " + pet)

#------------------------------------------------------------ example of class inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2


    def breathe(self):
        print(" le le hawa")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print(" Swim in the Water")

    def breathe(self):
        super().breathe()
        print(" super class breath called here ")


nemo = Fish()
nemo.swim()
nemo.breathe()