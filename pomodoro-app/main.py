
from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
DARK_BLUE = "#1C658C"
LIGHT_BLUE = "#398AB9"
BEIGE = "#D8D2CB"
GRAY = "#EEEEEE"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 8
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = 2 * 60
    short_break_sec = 1 * 60
    long_break_sec = 2 * 60
    if reps == 0:
        count_down(LONG_BREAK_MIN)
    elif reps % 2:
        count_down(SHORT_BREAK_MIN)
    else:
        count_down(WORK_MIN)
    reps -= 1

        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = floor(count / 60);
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60;
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    print(f"{count_min}:{count_sec}")    
    canvas.itemconfig(timer_label, text=f"{count_min}:{count_sec}")
    if count > 0:
        count -= 1
        window.after(1000, count_down, count)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BEIGE)
window

label_title = Label(text="Timer", fg=LIGHT_BLUE, font=(FONT_NAME, 35, "bold"), bg=BEIGE)
label_title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=BEIGE, highlightthickness=False)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_label = canvas.create_text(100, 130, text="00:00", fill=GRAY, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", bg=GRAY)
button_start.grid(column=0, row=2)
button_start.config(command=start_timer)
button_reset = Button(text="Reset", bg=GRAY)
button_reset.grid(column=2, row=2)
label_checkmarks = Label(text="✔✔✔✔", fg=DARK_BLUE, bg=BEIGE, font=(FONT_NAME, 15, "bold"))
label_checkmarks.grid(column=1, row=3)
# ✔
window.mainloop()