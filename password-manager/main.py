from tkinter import *
from tkinter import messagebox
from pathlib import Path
from json import *
from random import *
import pyperclip
PATH_SCRIPT = str(Path(__file__).parent.absolute())
IMAGE_PATH = fr'{PATH_SCRIPT}\logo.png'
FONT = ("Courier", 15, "normal")
PASSWORD_FILE = fr'{PATH_SCRIPT}\pw.json'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    num_letters = randint(8, 10)
    num_numbers = randint(2, 4)
    num_symbols = randint(2, 4)
    password = ""
    list_of_chars = [letters, numbers, symbols]
    password_list = []
    num_list = [num_letters, num_numbers, num_symbols]
    for idx, num in enumerate(num_list):
        for _ in range(num):
            password_list += choice(list_of_chars[idx])
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(END, string=password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    global website_entry, email_entry, password_entry
    # Get values from UI
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if not website or not email or not password:
        is_ok = messagebox.showerror(title="Error", message=f"Please fill out all fields")
        return
    is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered:\n Email: {email}\n Password: {password}\n Are you sure you want to save?")
    if not is_ok:
        return
    # Create a directory
    password_dict = {
        "website": website,
        "email": email,
        "password": password,
    }

    # Read JSON file
    passwords_dict = None
    try:
        with open(PASSWORD_FILE, "r") as file:
            passwords_dict = load(file)
    except FileNotFoundError:
        print("File doesn't exist, creating...")
    except JSONDecodeError:
        print('Decoding JSON has failed')
    except Exception as e:
        print(type(e))
        print(e.args)
    if not passwords_dict:
        passwords_dict = {
            "version": "1.0.0",
            "passwords": []
        }
    passwords_dict["passwords"].append(password_dict)
    # Write JSON file
    passwords_json = dumps(passwords_dict, indent=4)
    with open(PASSWORD_FILE, "w") as file:
            file.write(passwords_json)

    # Clear entry fields
    website_entry.delete(0, END)
    password_entry.delete(0, END)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    global website_entry, email_entry, password_entry
    # Get values from UI
    website = website_entry.get()
    if not website:
        messagebox.showerror(title="Error", message=f"Please provide a website to search for")
        return
    # Create an empty directory
    password_dict = {
        "website": "",
        "email": "",
        "password": "",
    }

    # Read JSON file
    passwords_dict = None
    try:
        with open(PASSWORD_FILE, "r") as file:
            passwords_dict = load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message=f"There are no passwords saved!")
        print("File doesn't exist, there are no passwords saved!")
    except JSONDecodeError:
        print('Decoding JSON has failed')
    except Exception as e:
        print(type(e))
        print(e.args)
    if not passwords_dict:
        return
    for password in passwords_dict["passwords"]:
            print(password)
            if website.lower() == password["website"].lower():
                email_entry.delete(0, END)
                email_entry.insert(0, string=password["email"])
                password_entry.delete(0, END)
                password_entry.insert(0, string=password["password"])
                pyperclip.copy(password["password"])
                return
    # website not found
    messagebox.showerror(title="Error", message=f"Password for given email not found!")
# ---------------------------- KEY EVENTS ------------------------------- #
def search_keyenter(e):
    search_password()
def generate_keyenter(e):
    generate_password()
def add_keyenter(e):
    save_password()

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=50)

# Logo Image
canvas = Canvas(width=200, height=200)
canvas.grid(column=0, row=0, columnspan=3, pady=(0, 50))
logo_img = PhotoImage(file=IMAGE_PATH)
canvas.create_image(100, 100, image=logo_img)

# website label
website_label = Label(text="Website:", font = FONT)
website_label.grid(column=0, row=1)
# website Entry
website_entry = Entry(width=23)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")
website_entry.focus()
# Search button
password_button = Button(text="Search", width=14, command=search_password)
password_button.grid(column=2, row=1, sticky="E")
password_button.bind("<Return>", search_keyenter)

# email label
email_label = Label(text="Email/Username:", font = FONT)
email_label.grid(column=0, row=2)
# email Entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "danielnavarrete.5@hotmail.com")

# password label
password_label = Label(text="Password:", font = FONT)
password_label.grid(column=0, row=3)
# password Entry
password_entry = Entry(width=23)
password_entry.grid(column=1, row=3, sticky="W")
# password Button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="E")
password_button.bind("<Return>", generate_keyenter)

# Add Button
add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
add_button.bind("<Return>", add_keyenter)



window.mainloop()
