from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.level = 0
        self.text = f"Level: {self.level}"
        self.hideturtle()
        self.pu()
        self.setpos(-x + 100, y - 30)
        self.color("white")
        self.write(self.text, align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.text = f"Level: {self.level}"
        self.write(self.text, align=ALIGNMENT, font=FONT)
    
    def write_centered(self, text, y, color):
        self.home()
        self.color(color)
        self.write(text, align=ALIGNMENT, font=FONT)