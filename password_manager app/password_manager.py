import random
import pyperclip
import json
from tkinter import *
from tkinter import messagebox

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# UI setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=GREEN)

canvas = Canvas(width=200, height=200, bg=GREEN, highlightthickness=0)
logo = PhotoImage(file="D:\python_mastery\password-manager-app\logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

text1 = Label(text="Website:",  font=(FONT_NAME, 15), bg=GREEN)
text1.grid(row=1, column=0)
text2 = Label(text="Email/User_name:",  font=(FONT_NAME, 15), bg=GREEN)
text2.grid(row=2, column=0)
text3 = Label(text="Password:",  font=(FONT_NAME, 15), bg=GREEN)
text3.grid(row=3, column=0)

web_entry = Entry(width=40, font=(FONT_NAME, 12))
web_entry.grid(row=1, column=1, pady=10)
web_entry.focus()
mail_entry = Entry(width=40, font=(FONT_NAME, 12))
mail_entry.grid(row=2, column=1, pady=10)
mail_entry.insert(0, "")
pass_entry = Entry(width=40, fg=RED, font=(FONT_NAME, 12, "bold"))
pass_entry.grid(row=3, column=1, pady=20, padx=20)

def password_generator():
    letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
        "x", "y", "z", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "M", "N", "B", "V", "C", "X", "Z"
    ]

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "@", "#", "$", "&", "*"]

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    pass_letters = [random.choice(letters) for _ in range(nr_letters)]
    pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = pass_letters + pass_numbers + pass_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

gen_pass = Button(text="Generate Password", bg="lightgray", font=(FONT_NAME, 12), bd=2, command=password_generator)
gen_pass.grid(row=3, column=2, padx=10)


def save():
    a = web_entry.get()
    b = mail_entry.get()
    c = pass_entry.get()

    saved_data = {
        a:{
            "email": b,
            "password": c,
        }
    } 

    if len(a) == 0 or len(c) == 0:
        messagebox.showwarning(title="Warning !! ", message="Fields can't be empty.")
    else:
        is_ok = messagebox.askokcancel(title="Are you sure?", message=f"Website: {a}\nUsername: {b}\nPassword: {c}")
        if is_ok:
            try:
                with open("data.json", mode="r") as data:  
                    d = json.load(data)      #reading old data
            except FileNotFoundError:
                with open("data.json", mode="w") as data:
                    json.dump(saved_data, data, indent=4)
            else:
                d.update(saved_data)         #update the old data with new one
                with open("data.json", mode="w") as data:
                    json.dump(d, data, indent=4)   #save updated data

            finally:
                    web_entry.delete(0, END)
                    pass_entry.delete(0, END)


add_button = Button(text="Add", width=40, bd=2, bg="lightgray", font=(FONT_NAME, 12), command=save)
add_button.grid(row=4, column=1)


def find_password():
    a = web_entry.get()
    with open("data.json") as show:
        exist_dict = json.load(show)
        if a in exist_dict:
            email = exist_dict[a]["email"]
            password = exist_dict[a]["password"]
            messagebox.showinfo(title=a, message=f"Email: {email}\nPassword: {password}")



search_button = Button(text="Search", bg="lightgray", width=16, font=(FONT_NAME, 12), bd=2, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()

