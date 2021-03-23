from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# #Password Generator Project
# def get_parameters():
#     get_parameters = True
#     gen_window = Toplevel()
#     gen_window.geometry('200x200')
#     gen_window.title("Password Parameters")
#     letter_char = Label(gen_window, text="How many letters?")
#     letter_char.grid(column=0, row=1)
#     letter_spinbox = Spinbox(gen_window, from_=1, to=10, width=5)
#     letter_spinbox.grid(column=2, row=1)
#     number_char = Label(gen_window, text="How many numbers?")
#     number_char.grid(column=0, row=2)
#     number_spinbox = Spinbox(gen_window, from_=0, to=10, width=5)
#     number_spinbox.grid(column=2, row=2)
#     symbol_char = Label(gen_window, text="How many symbols?")
#     symbol_char.grid(column=0, row=3)
#     symbol_spinbox = Spinbox(gen_window, from_=0, to=10, width=5)
#     symbol_spinbox.grid(column=2, row=3)
#     letter_num = int(letter_spinbox.get())
#     symbol_num = int(symbol_spinbox.get())
#     number_num = int(number_spinbox.get())
#     submit = Button(gen_window, text="Submit", command= lambda: generate_password(letter_num, symbol_num, number_num))
#     submit.grid(column=1, row=4)

def get_data():
    pass

def generate_password():


    print(letter_num, symbol_num, number_num)
    letterbank = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numberbank = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbolbank = ['!', '#', '$', '%', '&', '(', ')', '*', '+']





    letters = [random.choice(letterbank) for char in range(int(letter_spinbox.get()))]

    symbols = [random.choice(symbolbank) for char in range(int(symbol_spinbox.get()))]

    numbers = [random.choice(numberbank) for char in range(int(number_spinbox.get()))]

    password_list = letters + numbers + symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = site_entry.get().title()
    uname = uname_entry.get().title()
    password = pass_entry.get()
    new_data = {site: {
        "email": uname,
        "password": password
    }}
    if len(site) == 0 or len(uname) == 0 or len(password) == 0:
        messagebox.showerror(title="Oi Josuke!", message="You left fields empty! Isn't that wacky?")
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open('data.json', 'r') as data_file:

                data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            site_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')

def search():
    site = site_entry.get().title()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            site_data = data[site]
            print(data[site])
            messagebox.showinfo(title=f"{site} data", message=f"Username/email:{site_data['email']}\nPassword: {site_data['password']}")

    except FileNotFoundError:
        messagebox.showerror(title="Oi Josuke!", message="You don't have data yet! Isn't that wacky?")
    except KeyError:
        messagebox.showerror(title="Oi Josuke!", message="That site isn't in the data yet! Isn't that wacky?")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")

pass_img = PhotoImage(file='logo.png')
canvas = Canvas(width= 200, height=200)
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)
window.config(padx= 20, pady=20)

# Website label and entry width 35

site_label = Label(text="Website")
site_label.grid(column=0, row=1)
site_entry = Entry(width=33)
site_entry.grid(column=1, row=1, columnspan=1)
site_entry.focus()
search = Button(text="Search", width=15, bg="#EA5252", fg="#ffffff", command=search)
search.grid(column=2, row=1)
# Email/username label and entry width 35

uname_label = Label(text="Email/Username")
uname_label.grid(column=0, row=2)
uname_entry = Entry(width=52)
uname_entry.insert(0,"jrlewis84@gmail.com")
uname_entry.grid(column=1, row=2, columnspan=2)
# password label, entry width 21, and generate button
pass_label = Label(text="Password")
pass_label.grid(column=0, row=3)
pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3)
pass_button = Button(text="Generate Password", command=generate_password, bg="#EA5252", fg="#ffffff")
pass_button.grid(column=2, row=3)
# add button
add_button = Button(text="Add", width=44, command=save, bg="#EA5252", fg="#ffffff")
add_button.grid(column=1, row=4, columnspan=2)
# Parameters for password generation
parameters= Label(text="Parameters for Password Generation")
parameters.grid(column=0, row=5)
letter_char = Label(text="How many letters?")
letter_char.grid(column=0, row=6)
letter_spinbox = Spinbox(from_=1, to=10, width=5)
letter_spinbox.grid(column=2, row=6)
number_char = Label(text="How many numbers?")
number_char.grid(column=0, row=7)
number_spinbox = Spinbox(from_=0, to=10, width=5)
number_spinbox.grid(column=2, row=7)
symbol_char = Label(text="How many symbols?")
symbol_char.grid(column=0, row=8)
symbol_spinbox = Spinbox(from_=0, to=10, width=5)
symbol_spinbox.grid(column=2, row=8)
letter_num = int(letter_spinbox.get())
symbol_num = int(symbol_spinbox.get())
number_num = int(number_spinbox.get())
submit = Button(text="Submit", command=generate_password, bg="#EA5252", fg="#ffffff")
submit.grid(column=1, row=9)



window.mainloop()