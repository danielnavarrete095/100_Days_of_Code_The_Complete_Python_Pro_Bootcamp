from ctypes import alignment
from tkinter import *
from pathlib import Path
from json import *
PATH_SCRIPT = str(Path(__file__).parent.absolute())
IMAGE_PATH = fr'{PATH_SCRIPT}\logo.png'
FONT = ("Courier", 15, "normal")
PASSWORD_FILE = fr'{PATH_SCRIPT}\pw.json'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    global website_entry, email_entry, password_entry
    # Get values from UI
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

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
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

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
password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3, sticky="E")

# Add Button
add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")



window.mainloop()
