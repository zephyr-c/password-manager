from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

DEFAULT_EMAIL = "zephyr-c@email.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_nums = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_nums
    shuffle(password_list)

    password = ''.join(password_list)
    password_input.delete(0, 'end')
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def reset_form():
    website_input.delete(0, 'end')
    website_input.focus()
    password_input.delete(0, 'end')
    if user_input.get() != DEFAULT_EMAIL:
        user_input.delete(0, 'end')
        user_input.insert(0, DEFAULT_EMAIL)


def save_password():
    website = website_input.get()
    login_name = user_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": login_name,
            "password": password
        }
    }

    if not website or not password:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    else:
        # with open("data.json", "r") as file:
        try:
            data_file = open("data.json")
        except FileNotFoundError:
            data = new_data
        else:
            # Reading old data
            data = json.load(data_file)
            # Updating old data with new data
            data.update(new_data)

            data_file.close()
        finally:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

                reset_form()

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="No Data File Found", message="You haven't saved any passwords!")
    else:
        password_info = data.get(website, None)

        if not password_info:
            messagebox.showinfo(title="Password Not Found", message="You haven't saved a password for that website!")
        else:
            messagebox.showinfo(title=website, message=f"eMail: {password_info['email']}\n"
                                                       f"Password: {password_info['password']}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img, anchor="center")
canvas.grid(row=0, column=1)


# Labels
# Website Label
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

# User Info Label
user_label = Label(text="Email/Username: ")
user_label.grid(row=2, column=0)

# Password Label
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Customization Labels


# Input Fields
# Website Input Field
website_input = Entry(width=21)
website_input.focus()
website_input.grid(row=1, column=1)

# User Input Field
user_input = Entry(width=35)
user_input.insert(0, DEFAULT_EMAIL)
user_input.grid(row=2, column=1, columnspan=2)

# Password Input
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
# Search Button
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

# Generate Password Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

# Add Password Button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()
