from cgitb import text
from tkinter import *

input = None
label_result = None
def calculate():
    global input, label_result
    print("Calculate")
    miles = float(input.get())
    km = miles * 1.6
    label_result["text"] = str(km)
def main():
    global input, label_result
    window = Tk()
    # window.minsize(width=400, height=200)
    window.config(padx=10, pady=10)

    input = Entry()
    input.grid(column=1, row=0)
    input.insert(END, string="0")
    input.config(width=10)
    label_miles = Label(text="Miles", font=("Calibri", 12, "normal"))
    label_miles.grid(column=2, row=0)
    label_equal = Label(text="Is equal to", font=("Calibri", 12, "normal"))
    label_equal.grid(column=0, row=1)
    label_result = Label(text="0", font=("Calibri", 12, "normal"))
    label_result.grid(column=1, row=1)
    label_km = Label(text="Km", font=("Calibri", 12, "normal"))
    label_km.grid(column=2, row=1)
    
    button_calculate = Button(text="Calculate", command=calculate)
    button_calculate.grid(column=1, row=2)

    window.mainloop()
if __name__ == '__main__':
    main()