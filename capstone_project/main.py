BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas, random, time

to_learn= {}
random_french = {}
try:
    data = pandas.read_csv("new_learn_word.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def translate():
    global random_french, flip_timer
    window.after_cancel(flip_timer)
    random_french = random.choice(to_learn)
    print(random_french)
    canvas.itemconfig(card_title , text="French", fill="black")
    canvas.itemconfig(value, text=random_french["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(value, text=random_french["English"], fill="white")
    canvas.itemconfig(card_background, image= card_back_image)

def is_learn():
    to_learn.remove(random_french)
    data = pandas.DataFrame(to_learn)
    data.to_csv("new_learn_word.csv", index=False)
    translate()

window = Tk()
window.title("Flash card Project")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)



canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="card_front.png")
card_back_image =  PhotoImage(file="card_back.png")
card_background =canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial",40,"italic"))
value = canvas.create_text(400,263, text= "", font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)





cross_image =PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=translate)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="right.png")
check_button = Button(image=check_image, highlightthickness=0,command=is_learn)
check_button.grid(row=1, column=1)

# cross_image =PhotoImage(file="wrong.png")
# unknown_button = Button(image=cross_image, highlightthickness=0, command=translate)
# unknown_button.grid(row=1, column=0)
#
# check_image = PhotoImage(file="right.png")
# check_button = Button(image=check_image, highlightthickness=0,command=translate)
# check_button.grid(row=1, column=1)

# data = pandas.read_csv("french_words.csv")
# random_french = random.choice(data["French"])
# print(random_french)

translate()
window.mainloop()
