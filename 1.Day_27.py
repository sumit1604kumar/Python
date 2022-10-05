# # Tkinter and Python GUI
# from tkinter import *
# #-------------------------------------------------------------------------------------
# # window = tkinter.Tk() # object created from the class, the line below will run the loop, which will open the window page
# # window.title("My First GUI Program")
# # window.minsize(width=500, height=300)
# #
# # # Labels
# # my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# # my_label.pack()
# #
# # my_label["text"] = "New label name is Sumit"  # label updated to new value
# # my_label.config(text="My name is Anju")       # label again updated to the new value
# #
# # # Button
# # def button_click():
# #     new_text = input.get()
# #     my_label.config(text=new_text)
# #
# # button = tkinter.Button(text="Click Me", command=button_click)
# # button.pack()
# #
# # # Entry component
# # input = tkinter.Entry(width= 10)
# # input.pack()
# # print(input.get())
#
#
#
# #  test
# # def ee(a=1,b=2,c=3):
# #     print(a,b,c)
# # ee(b=10)
# #
# #
#
# # def add(*sum):  # unlimited arguments with asterik  --it is tuple
# #     total = 0
# #     for n in sum:
# #         total += n
# #     print(total)
# # add(5,10,20,25, 40)
# #
# # def calculate(n, **kwargs): # it is dict
# #     for key, value in kwargs.items():
# #         print(key, value)
# #
# #
# #     print(kwargs['add'])
# #     n += kwargs["add"]
# #     print(n)
# # calculate(2, add=3, multiply= 5)
# #
# # class Car:
# #
# #     def __init__(self, **kwargs):
# #         self.make = kwargs.get("make")    # advantage of using get, if no value it will return None, unless of any error.
# #         self.model = kwargs.get("model")
# #
# # my_car = Car(make="Nissan")
# # print(my_car.model)
# # foo(4, 9)
# #--------------------------
#
#
# # def all_aboard(a, *args, **kw):
# #     print(a, args, kw)
# #
# #
# # all_aboard(4, 7, 3, 0, x=10, y=64)
#
#
# #---------------------------new demo------------
#
# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# #Buttons
# def action():
#     print("Do something")
#
# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()
#
#
#pack, place and grid
# place have x and y vlaue .place(x=0, y=0) precise co-ordinates, grid ->
#
# window.mainloop()

# ------------------------------------------------------------------------------------------------------------------
# Miles to Kms Project
import tkinter
from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=320, height=200)
window.config(padx=10, pady=10)

def action():
    miles = float(input.get())
    kilometer = miles * 1.60
    result.config(text=f"{kilometer:.2f}")



my_label = tkinter.Label(text="is equal to ", font=("courier", 12, "bold"))
my_label.grid(column=1, row= 2)

miles_label = tkinter.Label(text="Miles ", font=("courier", 12, "bold"))
miles_label.grid(column=3, row= 1)
miles_label.config(padx=10, pady=10)

km_label = tkinter.Label(text="Km ", font=("courier", 12, "bold"))
km_label.grid(column=3, row= 2)

input = Entry(width=10)
print(input.get())
input.grid(column=2, row=1)

result = tkinter.Label(text="0 ", font=("courier", 12, "bold"))
result.grid(column=2, row=2)



button = Button(text="Calculate", command=action)
button.grid(column=2, row=3)

window.mainloop()

