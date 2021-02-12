from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Get hold of text in all entry boxes


# Write ' | ' separated values to data.txt
# Clear website and password fields




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
user_input.insert(0, "zephyrworthington@gmail.com")
user_input.grid(row=2, column=1, columnspan=2)

# Password Input
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
# Generate Password Button
generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)

# Add Password Button
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()
