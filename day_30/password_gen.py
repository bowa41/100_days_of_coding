from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    pw_entry.delete(0, END)
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    pw_entry.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pw_entry.get()
    new_data = {
        website : {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pw_entry.delete(0, END)

# ---------------------------- Search for PASSWORD Entry--------------------- #
def find_password():
    website = (website_entry.get())
    try:
        with open("data.json", "r") as data_file:
        # Reading old data
            data = json.load(data_file)
        pyperclip.copy(data[website]["password"])
    except FileNotFoundError:
        messagebox.showinfo(title="No File Exists",  message="No password file has been found.")
    except KeyError:
        messagebox.showinfo(title="No Website Exists", message="No website entry exists for that name.")
    else:
        messagebox.showinfo(title=f"{website} info",  message=f"Username: {data[website]["email"]}\n "
                                                          f"Password: {data[website]["password"]}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=20, bg="white")


canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
logo = PhotoImage(file="../day_29/logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)
pw_label = Label(text="Password:", bg="white")
pw_label.grid(column=0, row=3)

#Buttons

generate_button = Button(text="Generate", command=generate_pw, highlightthickness=0, bg="white")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=37, command=save, highlightthickness=0, bg="white")
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password, highlightthickness=0, bg="white")
search_button.grid(column=2, row=1)


#Entries
website_entry = Entry(width=34,justify="left")
website_entry.insert(END, string="")
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=44, justify="left")
email_entry.insert(0, string="bowa41@att.net")
email_entry.grid(column=1, row=2, columnspan=2)

pw_entry = Entry(width=34, justify="left")
pw_entry.grid(column=1, row=3)

window.mainloop()