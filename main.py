from tkinter import *
DEFAULT_EMAIL = "zephyrworthington@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
    entry = [website, login_name, password]
    reset_form()

    with open("data.txt", "a") as file:
        file.write(' | '.join(entry))
        file.write('\n')





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
generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)

# Add Password Button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()
