from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
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

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email_username = email_and_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username}\nPassword: "
                                                      f"{password} \n Is it ok to save? ")

        if is_ok:
            with open("data.txt", 'a') as data_file:
                data_file.write(f"{website} | {email_username} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Website: ")
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.config(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_and_username_label = Label()
email_and_username_label.config(text="Email/Username: ")
email_and_username_label.grid(column=0, row=2)

email_and_username_entry = Entry()
email_and_username_entry.config(width=35)
email_and_username_entry.grid(column=1, row=2, columnspan=2)
email_and_username_entry.insert(0, "@gmail.com")

password_label = Label()
password_label.config(text="Password: ")
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3, columnspan=1)

generate_password_button = ttk.Button()
generate_password_button.config(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = ttk.Button()
add_button.config(text="Add")
add_button.config(width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()