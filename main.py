from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

DEFAULT_EMAIL = "zephyrworthington@gmail.com"

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

    if not website or not password:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Confirm details: \nEmail/Username: {login_name} "
                                                      f"\nPassword: {password} \nOk to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f'{website} | {login_name} | {password}\n')
                reset_form()


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

# Input Fields
# Website Input Field
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

# User Input Field
user_input = Entry(width=35)
user_input.insert(0, DEFAULT_EMAIL)
user_input.grid(row=2, column=1, columnspan=2)

# Password Input
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
# Generate Password Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

# Add Password Button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()
