from textwrap import fill
from tkinter import *
from tkinter import messagebox
from numpy import flip
from pandas import read_csv, DataFrame
from random import randint, choice
BACKGROUND_COLOR = "#B1DDC6"
FLASH_CARD_IMAGE = r"images\card_front.png"
FLIP_CARD_IMAGE = r"images\card_back.png"
CHECK_IMAGE = r"images\right.png"
CROSS_IMAGE = r"images\wrong.png"
GERMAN_WORDS_FILE = r"data\german_words.csv"
WORDS_TO_LEARN_FILE = r"data\german_words_to_learn.csv"
FONT = "Ariel"
ORIGIN_LANGUAGE =  "German"
TRANSLATION_LANGUAGE = "English"

word_text = ""
translation_text = ""
flash_card_canvas = None
current_word = ""
current_translation = ""
current_word = ""
current_card = {ORIGIN_LANGUAGE: "", TRANSLATION_LANGUAGE: ""}
front_card_image = None
back_card_image = None
flip_timer = None

def get_random_word():
    global word_text, current_card
    # word, translation = choice(list(data_list.items()))
    word = choice(data_list)
    # print(translation)
    print(word)
    current_card[ORIGIN_LANGUAGE] = word[ORIGIN_LANGUAGE]
    current_card[TRANSLATION_LANGUAGE] = word[TRANSLATION_LANGUAGE]
    # return (word["German"], word["English"])
def next_card():
    global flash_card_canvas, current_card, front_card_img, flip_timer
    flash_card_canvas.after_cancel(flip_timer)
    # word, translation = get_random_word()
    get_random_word()
    flash_card_canvas.itemconfig(image_container,image=front_card_img)
    flash_card_canvas.itemconfig(word_text, text=ORIGIN_LANGUAGE, fill = "black")
    flash_card_canvas.itemconfig(translation_text, text=current_card[ORIGIN_LANGUAGE], fill = "black")
    flip_timer = flash_card_canvas.after(3000, flip_card)

def flip_card():
    global flash_card_canvas, current_card, back_card_img
    flash_card_canvas.itemconfig(image_container,image=back_card_img)
    flash_card_canvas.itemconfig(word_text, text=TRANSLATION_LANGUAGE, fill = "white")
    flash_card_canvas.itemconfig(translation_text, text=current_card[TRANSLATION_LANGUAGE], fill = "white")

def event_checkmark_button():
    global data_list
    # Remove current word from list
    # card = {"German": current_card["word"], "English": current_card["translation"]}
    data_list.remove(current_card)
    # Call next card
    next_card()
    pass
def event_cross_button():
    # Call next card
    next_card()

def on_closing():
    global window, data_list
    # Save things to learn csv
    df = DataFrame(data_list)
    df.to_csv(WORDS_TO_LEARN_FILE, index=False)
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.protocol("WM_DELETE_WINDOW", on_closing)

# flash card canvas
flash_card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_canvas.grid(column=0, row=0, columnspan=2)
front_card_img = PhotoImage(file = FLASH_CARD_IMAGE)
back_card_img = PhotoImage(file = FLIP_CARD_IMAGE)
image_container = flash_card_canvas.create_image(400, 263, image=front_card_img)
word_text = flash_card_canvas.create_text(400, 150, text=ORIGIN_LANGUAGE, fill="black", font=(FONT, 40, "italic"))
translation_text = flash_card_canvas.create_text(400, 263, text="Word", fill="black", font=(FONT, 60, "bold"))
# buttons
check_img = PhotoImage(file=CHECK_IMAGE)
check_button = Button(image=check_img, highlightthickness=0, borderwidth=0, command=event_checkmark_button)
check_button.grid(column=0, row=1)
cross_img = PhotoImage(file=CROSS_IMAGE)
cross_button = Button(image=cross_img, highlightthickness=0, borderwidth=0, command=event_cross_button)
cross_button.grid(column=1, row=1)


# Read csv file
data = read_csv(GERMAN_WORDS_FILE)
# print(data)
# data_list = {row.German:row.English for (index, row) in data.iterrows()}
data_list = data.to_dict(orient="records")
# print(data_list)
flip_timer = flash_card_canvas.after(3000, flip_card)
next_card()


window.mainloop()