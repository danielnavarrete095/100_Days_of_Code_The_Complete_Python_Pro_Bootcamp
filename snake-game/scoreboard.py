from turtle import Turtle

ALIGNMENT = "center"
FONT = "Calibri", 15, "bold"
class Scoreboard(Turtle):
    def __init__(self, y):
        super().__init__()
        self.score = 0
        self.text = f"Score: {self.score}"
        self.hideturtle()
        self.pu()
        self.sety(y - 30)
        self.color("white")
        self.write(self.text, align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.text = f"Score: {self.score}"
        self.write(self.text, align=ALIGNMENT, font=FONT)
    
    def write_centered(self, text, y):
        self.home()
        self.write(text, align=ALIGNMENT, font=FONT)