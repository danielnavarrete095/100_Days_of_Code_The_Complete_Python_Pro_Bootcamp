from cgitb import text
from distutils import command
from tkinter import *
from tkinter import font

my_label = None
input = None
input_value = ""
counter = 0

def button_clicked():
    global counter, my_label
    print("I got clicked!")
    counter += 1
    my_label["text"] = f"Times clicked = {counter}"

def get_entry_value():
    global input
    my_label["text"] = input.get()

def main():
    global counter, my_label, input
    window = Tk()
    window.title("First GUI")
    window.minsize(width=500, height=300)
    window.config(padx=100, pady=20)

    # Label
    my_label = Label(text=f"Times clicked = {counter}", font=("Calibri", 24, "bold"))
    # my_label.pack()
    # my_label.place(x=0, y=0)
    my_label.grid(column=0, row=0)
    my_label.config(padx=50, pady = 50)

    # my_label["text"] = "New Text"
    # my_label.config(text="New New Text")
    
    # Button
    button = Button(text="Click me!", command=button_clicked)
    button.grid(column=1, row=1)
    # button.pack()
    button1 = Button(text="Click me!", command=get_entry_value)
    button1.grid(column=2, row=0)
    # button1.pack()

    # Entry
    input = Entry()
    input.grid(column=3, row=2)
    # input.pack()

    window.mainloop()
if __name__ == '__main__':
    main()