# Password Manager with GUI Tkinter

from tkinter import *
from tkinter import messagebox

import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    print(password_list)

    password = "".join(password_list)
    password_text.insert(0,password)


YELLOW = "#f7f5dd"
# Background Creation
window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=200,bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Save Password after clicking Add button

def save():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword:{password}\n Is it ok to save ?")
        if is_ok:
            with open("mail_id.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_text.delete(0, END)
                password_text.delete(0,END)













#labels
website_label = Label(text="Website:", bg=YELLOW)
website_label.grid(column=0, row= 1)
email_label = Label(text="Email/Username:", bg=YELLOW)
email_label.grid(column=0, row= 2)
Password_label = Label(text="Password:", bg=YELLOW)
Password_label.grid(column=0, row= 3)

#Text Box
website_text = Entry(width=35)
website_text.grid(column=1, columnspan= 2, row= 1)
website_text.focus()
email_text = Entry(width=35)
email_text.grid(column=1, columnspan= 2, row= 2)
email_text.insert(0, "sumit.st.michel@gmail.com")
password_text= Entry(width=18)
password_text.grid(column=1, row=3)

# Button
password_generate = Button(text="Generate Password", command=generate_password)
password_generate.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, columnspan=2, row=4)



window.mainloop()