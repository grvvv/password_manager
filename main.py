from tkinter import *
from tkinter import messagebox  # since it's not a class
from pass_generator import Password
import pyperclip
import json
from search import Search
FONT = ("Times New Roman", 13)


# ---------------------------- SEARCH MANAGER ------------------------------- #
def find_password():
    site_input = site.get()
    Search(site_input)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    p_input.delete(0, 'end')
    new = Password()
    new_password = new.generate()
    p_input.insert(0, new_password)
    pyperclip.copy(new_password)  # copies new_password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    site_input = site.get()
    user_mail = u_input.get().lower()
    pass_input = p_input.get()
    new_data = {
        site_input: {
            "email": user_mail,
            "password": pass_input
        }
    }
    if site_input == "" or pass_input == "":
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)            # reads json data and data variable stores a simple nested dic

        except FileNotFoundError:
            with open("data.json", mode="w") as new_file:
                json.dump(new_data, new_file, indent=4)  # creates a json file if not exists

        else:
            data.update(new_data)                  # updates dictionary
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)        # updates new data in json file
        finally:
            site.delete(0, 'end')
            p_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("Password Manager")
win.config(padx=50, pady=50, bg="#FFFACD")

lock = Canvas(width=200, height=200, bg="#FFFACD", highlightthickness=0)
lock_image = PhotoImage(file="../password-manager-start/logo.png")
lock.create_image(100, 100, image=lock_image)
lock.grid(column=1, row=0)

# Labels
website = Label(bg="#FFFACD")
website.config(text="Website: ", font=FONT)
website.grid(column=0, row=1)

user = Label(bg="#FFFACD")
user.config(text="Email/Username: ", font=FONT)
user.grid(column=0, row=2)

password = Label(bg="#FFFACD")
password.config(text="Password: ", font=FONT)
password.grid(column=0, row=3)

# Buttons
search = Button(command=find_password, bg="#6495ED")
search.config(text="Search", font=FONT)
search.grid(column=2, row=1, sticky="EW")

generate = Button(command=generate_password)
generate.config(text="Generate Password", font=FONT)
generate.grid(column=2, row=3, sticky="EW")

add = Button(width=36, command=save)
add.config(text="Add", font=FONT)
add.grid(column=1, row=4, columnspan=2, sticky="EW")

# Entries
site = Entry(width=32)
site.focus()
site.grid(column=1, row=1, sticky="W")

u_input = Entry(width=35)
u_input.insert(0, "gauravchindarkar45@gmail.com")
u_input.grid(column=1, row=2, columnspan=2, sticky="EW")

p_input = Entry(width=32, show="*")
p_input.grid(column=1, row=3, sticky="W")

win.mainloop()
