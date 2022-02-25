from textwrap import fill
from tkinter import *
from numpy import flip
from pandas import read_csv, DataFrame
from random import randint, choice
BACKGROUND_COLOR = "#B1DDC6"
FLASH_CARD_IMAGE = r"images\card_front.png"
FLIP_CARD_IMAGE = r"images\card_back.png"
CHECK_IMAGE = r"images\right.png"
CROSS_IMAGE = r"images\wrong.png"
GERMAN_WORDS_FILE = r"data\german_words.csv"
FONT = "Ariel"
ORIGIN_LANGUAGE =  "German"
TRANSLATION_LANGUAGE = "English"

word_text = ""
translation_text = ""
flash_card_canvas = None
current_word = ""
current_translation = ""
front_card_image = None
back_card_image = None

def get_random_word():
    global word_text, current_word, current_translation
    # word, translation = choice(list(data_dict.items()))
    word = choice(data_dict)
    # print(translation)
    print(word)
    current_word = word["German"]
    current_translation = word["English"]
    # return (word["German"], word["English"])

def next_card():
    global flash_card_canvas, current_word, front_card_img
    # word, translation = get_random_word()
    get_random_word()
    flash_card_canvas.itemconfig(image_container,image=front_card_img)
    flash_card_canvas.itemconfig(word_text, text=ORIGIN_LANGUAGE, fill = "black")
    flash_card_canvas.itemconfig(translation_text, text=current_word, fill = "black")
    flash_card_canvas.after(3000, flip_card)

def flip_card():
    global flash_card_canvas, current_translation, back_card_img
    flash_card_canvas.itemconfig(image_container,image=back_card_img)
    flash_card_canvas.itemconfig(word_text, text=TRANSLATION_LANGUAGE, fill = "white")
    flash_card_canvas.itemconfig(translation_text, text=current_translation, fill = "white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

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
check_button = Button(image=check_img, highlightthickness=0, borderwidth=0, command=next_card)
check_button.grid(column=0, row=1)
cross_img = PhotoImage(file=CROSS_IMAGE)
cross_button = Button(image=cross_img, highlightthickness=0, borderwidth=0, command=next_card)
cross_button.grid(column=1, row=1)


# Read csv file
data = read_csv(GERMAN_WORDS_FILE)
# print(data)
# data_dict = {row.German:row.English for (index, row) in data.iterrows()}
data_dict = data.to_dict(orient="records")
# print(data_dict)
next_card()


window.mainloop()